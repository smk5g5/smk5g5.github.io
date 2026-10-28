"""Replace only the dedicated public website checkout with generated files."""
from pathlib import Path
import os, shutil
source = Path(os.environ["QUARTO_PUBLIC_OUTPUT"]).resolve()
target = Path(os.environ["PUBLIC_WEBSITE_CHECKOUT"]).resolve()
assert (source / "index.html").is_file(), "Missing generated website"
assert (target / ".git").is_dir(), "Target must be a dedicated Git checkout"
assert source != target and source not in target.parents and target not in source.parents
# Preserve an existing custom-domain declaration, if one is configured.
cname = (target / "CNAME").read_bytes() if (target / "CNAME").is_file() else None
for path in target.iterdir():
    if path.name == ".git":
        continue
    if path.is_dir() and not path.is_symlink():
        shutil.rmtree(path)
    else:
        path.unlink()
shutil.copytree(source, target, dirs_exist_ok=True)
(target / ".nojekyll").touch()
if cname is not None:
    (target / "CNAME").write_bytes(cname)
print("Copied generated output to dedicated public website checkout.")
