"""Download versioned CC BY papers and freeze exact page text as the environment.

# Sources retain their authors' CC BY 4.0 license; attribution is in each snapshot.
# Text extraction: pypdf (BSD-3-Clause), https://github.com/py-pdf/pypdf
"""

import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from hashlib import sha256
import importlib.metadata
import json
from pathlib import Path
import time

from bs4 import BeautifulSoup
from pypdf import PdfReader
import requests

ROOT = Path(__file__).resolve().parents[1]


def download(url):
    for attempt in range(3):
        try:
            response = requests.get(url, timeout=60, headers={"User-Agent": "PaperReviewAgent-M2/0.1 (educational snapshot)"})
            response.raise_for_status()
            return response
        except requests.RequestException:
            if attempt == 2:
                raise
            time.sleep(2 ** (attempt + 1))


def freeze_one(task):
    identifier, task_id = task["arxiv_id"], task["id"]
    snapshot_path = ROOT / "data/eval/papers" / f"{task_id}.json"
    if snapshot_path.exists():
        snapshot = json.loads(snapshot_path.read_text(encoding="utf-8"))
        if snapshot["arxiv_id"] != identifier:
            raise ValueError(f"Existing {task_id} has a different source; refusing to overwrite")
    else:
        source_url = f"https://arxiv.org/abs/{identifier}"
        soup = BeautifulSoup(download(source_url).text, "html.parser")
        license_url = next((a["href"] for a in soup.find_all("a", href=True)
                            if "creativecommons.org/licenses/by/4.0" in a["href"]), None)
        if not license_url:
            raise ValueError(f"CC BY 4.0 not confirmed for {identifier}; no snapshot written")
        title = soup.find("meta", attrs={"name": "citation_title"})["content"]
        authors = [m["content"] for m in soup.find_all("meta", attrs={"name": "citation_author"})]
        pdf_path = ROOT / "data/downloads" / f"{identifier}.pdf"
        pdf_path.parent.mkdir(parents=True, exist_ok=True)
        if not pdf_path.exists():
            content = download(f"https://arxiv.org/pdf/{identifier}").content
            if not content.startswith(b"%PDF"):
                raise ValueError(f"Not a PDF: {identifier}")
            pdf_path.write_bytes(content)
        reader = PdfReader(pdf_path)
        pages = [p.extract_text() or "" for p in reader.pages]
        if not any(p.strip() for p in pages):
            raise ValueError(f"No extractable text: {identifier}")
        snapshot = {"arxiv_id": identifier, "title": title, "authors": authors,
                    "source_url": source_url, "pdf_url": f"https://arxiv.org/pdf/{identifier}",
                    "license": "CC-BY-4.0", "license_url": license_url,
                    "modification": "PDF text extracted by page; images and layout omitted.",
                    "parser": f"pypdf=={importlib.metadata.version('pypdf')}",
                    "pdf_sha256": sha256(pdf_path.read_bytes()).hexdigest(),
                    "frozen_at": datetime.now(timezone.utc).isoformat(), "pages": pages}
        snapshot_path.parent.mkdir(parents=True, exist_ok=True)
        snapshot_path.write_text(json.dumps(snapshot, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Frozen {task_id}: {snapshot['title']} ({len(snapshot['pages'])} pages)", flush=True)
    return {**task, "title": snapshot["title"], "paper_path": f"papers/{task_id}.json",
            "snapshot_sha256": sha256(snapshot_path.read_bytes()).hexdigest(),
            "instructions_version": "m2-v1", "reference_score": None}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workers", type=int, default=2)
    args = parser.parse_args()
    selected = json.loads((ROOT / "data/selection.json").read_text(encoding="utf-8"))
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        tasks = list(pool.map(freeze_one, selected))
    path = ROOT / "data/eval/tasks.jsonl"
    content = "".join(json.dumps(t, ensure_ascii=False) + "\n" for t in tasks)
    if path.exists() and path.read_text(encoding="utf-8") != content:
        raise ValueError("Manifest differs from existing freeze; refusing to overwrite")
    path.write_text(content, encoding="utf-8")
    print(f"Frozen manifest: {path}; {len(tasks)} distinct paper tasks")


if __name__ == "__main__":
    main()
