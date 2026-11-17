"""Check this repository's skill entry point and inline Markdown file links."""

from pathlib import Path
import re
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "project-walkthrough"
LINK = re.compile(r"\[[^\]\n]+\]\(([^)\n]+)\)")


def main():
    entry = SKILL / "SKILL.md"
    text = entry.read_text(encoding="utf-8")
    header = re.match(r"\A---\n(.+?)\n---\n", text, flags=re.DOTALL)
    if not header:
        raise SystemExit("SKILL.md: missing YAML frontmatter")

    metadata = header.group(1)
    if not re.search(rf"^name: {re.escape(SKILL.name)}$", metadata, flags=re.MULTILINE):
        raise SystemExit("SKILL.md: name must match the skill directory")
    description = re.search(r"^description:[ \t]*([^\n]+)$", metadata, flags=re.MULTILINE)
    if not description or not 1 <= len(description.group(1).strip()) <= 1024:
        raise SystemExit("SKILL.md: description must have 1–1024 characters")

    for document in ROOT.rglob("*.md"):
        for link in LINK.findall(document.read_text(encoding="utf-8")):
            target = urlsplit(link.strip("<>"))
            if target.scheme in {"https", "http"}:
                continue
            if target.scheme or target.netloc or target.path.startswith("/"):
                raise SystemExit(f"{document.relative_to(ROOT)}: expected a relative link")
            if target.path:
                path = (document.parent / unquote(target.path)).resolve()
                scope = SKILL if document.is_relative_to(SKILL) else ROOT
                if not path.is_relative_to(scope) or not path.exists():
                    raise SystemExit(f"{document.relative_to(ROOT)}: broken link {link}")

    print("Skill entry point and Markdown file links are valid.")


if __name__ == "__main__":
    main()
