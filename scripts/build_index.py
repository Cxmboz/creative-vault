"""Compile every note's header block into index.json and report schema problems.

Usage:  python scripts/build_index.py      (run from the vault folder)
No third-party packages needed.
"""
import json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {".obsidian", ".git", "_templates", ".trash", "scripts"}
REQUIRED = {
    "reference": ["source_url", "license", "reuse"],
    "asset": ["source_url", "license", "reuse", "local_path"],
}
REUSE_FOR = {
    "CC0": "free", "public-domain": "free", "CC-BY-4.0": "credit-required",
    "CC-BY-SA": "credit-required", "CC-BY-NC": "reference-only", "CC-BY-ND": "reference-only",
    "proprietary": "reference-only", "unknown": "reference-only",
}


def parse_value(v):
    v = v.strip()
    if v.startswith("[") and v.endswith("]"):
        return [x.strip().strip("'\"") for x in v[1:-1].split(",") if x.strip()]
    if v.lower() in ("true", "false"):
        return v.lower() == "true"
    return v.strip("'\"")


def frontmatter(text):
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    meta, key = {}, None
    for line in text[3:end].splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if m:
            key, val = m.group(1), m.group(2)
            meta[key] = parse_value(val) if val.strip() else ""
        elif key and line.strip().startswith("- "):
            if not isinstance(meta.get(key), list):
                meta[key] = []
            meta[key].append(line.strip()[2:].strip().strip("'\""))
    return meta, text[end + 4:]


def main():
    entries, problems = [], []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            if not fn.endswith(".md") or fn in ("README.md", "AGENTS.md", "CLAUDE.md"):
                continue
            path = os.path.join(dirpath, fn)
            rel = os.path.relpath(path, ROOT).replace(os.sep, "/")
            with open(path, encoding="utf-8") as f:
                meta, body = frontmatter(f.read())
            if not meta:
                problems.append(f"{rel}: no header block")
                continue
            t = meta.get("type", "")
            for field in REQUIRED.get(t, []):
                if not meta.get(field):
                    problems.append(f"{rel}: missing {field}")
            lic, reuse = meta.get("license"), meta.get("reuse")
            if lic in REUSE_FOR and reuse and reuse != REUSE_FOR[lic] and reuse != "do-not-use":
                problems.append(f"{rel}: reuse '{reuse}' does not match license '{lic}' (expected '{REUSE_FOR[lic]}')")
            summary = next((ln.strip() for ln in body.splitlines()
                            if ln.strip() and not ln.startswith(("#", "|", "!", "-", ">"))), "")
            entries.append({
                "path": rel, "title": meta.get("title") or fn[:-3], "type": t,
                "domain": meta.get("domain", []), "tags": meta.get("tags", []),
                "tradition": meta.get("tradition", ""), "part": meta.get("part", ""),
                "license": lic or "", "reuse": reuse or "", "source_url": meta.get("source_url", ""),
                "local_path": meta.get("local_path", ""), "author": meta.get("author", ""),
                "verified": meta.get("verified", False), "status": meta.get("status", ""),
                "links": sorted(set(re.findall(r"\[\[([^\]|#]+)", body))),
                "summary": summary[:240],
            })
    entries.sort(key=lambda e: e["path"])
    with open(os.path.join(ROOT, "index.json"), "w", encoding="utf-8", newline="\n") as f:
        json.dump(entries, f, indent=1, ensure_ascii=False)
        f.write("\n")
    unverified = sum(1 for e in entries if e["type"] not in ("moc",) and not e["verified"])
    print(f"index.json: {len(entries)} notes, {unverified} unverified (excluding index notes)")
    for p in problems:
        print("WARNING", p)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
