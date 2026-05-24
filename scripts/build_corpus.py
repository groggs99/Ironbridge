"""Build a simple processed corpus from raw markdown/text research files.

This script is intentionally lightweight for v0. Drop Claude/manual research notes into
`data/raw/claude_research/` as .md or .txt files, then run:

    python scripts/build_corpus.py

It creates JSONL chunks in `data/processed/corpus_chunks.jsonl`.
"""

from __future__ import annotations

import json
from pathlib import Path

RAW_DIR = Path("data/raw/claude_research")
OUT_DIR = Path("data/processed")
OUT_FILE = OUT_DIR / "corpus_chunks.jsonl"

CHUNK_SIZE = 1800
OVERLAP = 250


def chunk_text(text: str, chunk_size: int = CHUNK_SIZE, overlap: int = OVERLAP) -> list[str]:
    text = text.strip()
    if not text:
        return []

    chunks: list[str] = []
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)
        if end == len(text):
            break
        start = max(0, end - overlap)
    return chunks


def infer_ecosystem(path: Path, text: str) -> str:
    blob = f"{path.name}\n{text[:500]}".lower()
    if "zcash" in blob or "zec" in blob or "zcg" in blob:
        return "zcash"
    if "near" in blob or "intents" in blob or "house of stake" in blob:
        return "near"
    if "ironclaw" in blob or "openclaw" in blob:
        return "ironclaw"
    return "unknown"


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    records = []
    for path in sorted(RAW_DIR.glob("**/*")):
        if path.suffix.lower() not in {".md", ".txt"}:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        ecosystem = infer_ecosystem(path, text)
        for idx, chunk in enumerate(chunk_text(text)):
            records.append(
                {
                    "source_file": str(path),
                    "chunk_id": f"{path.stem}-{idx:04d}",
                    "ecosystem": ecosystem,
                    "text": chunk,
                }
            )

    with OUT_FILE.open("w", encoding="utf-8") as f:
        for record in records:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")

    print(f"Wrote {len(records)} chunks to {OUT_FILE}")


if __name__ == "__main__":
    main()
