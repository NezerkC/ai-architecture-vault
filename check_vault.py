"""Vault lint: broken wikilinks, orphan notes, missing/BOM frontmatter. Exit 1 on errors.

Usage: python check_vault.py
"""
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).parent
# Notes allowed to have no inbound wikilinks (entry points or non-vault docs).
ENTRY_POINTS = {"Indice General", "README", "CLAUDE", "AGENTS"}
LINK = re.compile(r"\[\[([^\]|#]+)")
CODE = re.compile(r"```.*?```|`[^`\n]*`", re.S)


def tracked_md():
    out = subprocess.check_output(["git", "ls-files", "*.md"], cwd=ROOT, text=True)
    return [ROOT / f for f in out.splitlines()]


def main():
    files = tracked_md()
    # Only vault notes participate in the link graph; skill references are plain docs.
    notes = [p for p in files if "references" not in p.parts]
    names = {p.stem for p in notes if p.stem != "SKILL"}
    inbound = {n: 0 for n in names}
    errors = []

    for p in files:
        raw = p.read_bytes()
        rel = p.relative_to(ROOT).as_posix()
        if raw.startswith(b"\xef\xbb\xbf"):
            errors.append(f"BOM breaks frontmatter: {rel}")
        if p not in notes:
            continue
        text = raw.decode("utf-8", errors="replace")
        if p.stem not in ENTRY_POINTS | {"LICENSE"} and not text.startswith("---"):
            errors.append(f"missing frontmatter: {rel}")
        if p.name == "SKILL.md":
            head = text.split("---")[1] if text.startswith("---") else ""
            for key in ("name:", "description:"):
                if not re.search(rf"^{key}", head, re.M):
                    errors.append(f"SKILL.md without '{key[:-1]}': {rel}")
        for target in LINK.findall(CODE.sub("", text)):
            target = target.strip().split("/")[-1]
            if target in inbound:
                inbound[target] += (target != p.stem)
            else:
                errors.append(f"broken link [[{target}]] in {rel}")

    errors += [f"orphan note (no inbound links): {n}" for n, c in sorted(inbound.items())
               if c == 0 and n not in ENTRY_POINTS]

    print("\n".join(errors) or f"OK: {len(notes)} notes, 0 issues")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
