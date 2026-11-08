"""Check that every source_url in index.json still answers. Run build_index.py first.

Usage:  python scripts/check_links.py
"""
import json, os, sys, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def status(url):
    req = urllib.request.Request(url, method="GET", headers={"User-Agent": "creative-vault-linkcheck"})
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code
    except Exception as e:  # network errors
        return f"error: {e.__class__.__name__}"


def main():
    with open(os.path.join(ROOT, "index.json"), encoding="utf-8") as f:
        entries = json.load(f)
    bad = 0
    for e in entries:
        url = e.get("source_url")
        if not url:
            continue
        s = status(url)
        ok = isinstance(s, int) and s < 400
        bad += not ok
        print(("ok  " if ok else "FAIL"), s, e["path"], url)
    print(f"{bad} broken link(s)")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
