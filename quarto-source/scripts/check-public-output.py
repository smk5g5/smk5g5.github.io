from pathlib import Path
import sys
root = Path(sys.argv[1] if len(sys.argv) > 1 else "_site")
required = ["index.html", "publications.html", "software.html", "blog.html", "contact.html", "about.html", "posts/before-the-heatmap/index.html", "assets/anatomy-method-header.webp"]
for name in required:
    assert (root / name).is_file(), f"Missing generated file: {name}"
for file in root.rglob("*.html"):
    text = file.read_text()
    assert "My work connects tumor heterogeneity" not in text, file
    assert "Download CV" not in text, file
for pattern in ["*.qmd", "*.lr", "*.tex", "*.pdf", ".env"]:
    assert not list(root.rglob(pattern)), f"Unexpected source/private file in output: {pattern}"
print("Public output checks passed.")
