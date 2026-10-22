#!/usr/bin/env python3
"""Rebuild the standalone, nested, and Netlify variants from external-index.html."""
from __future__ import annotations
import base64
import mimetypes
import re
import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "external-index.html"
source = SOURCE.read_text(encoding="utf-8")

# The project-root copy keeps relative img/ and fonts/ paths.
# The nested copy lives in /external and reaches shared project assets one level up.
nested = source.replace("./img/", "../img/").replace("./fonts/", "../fonts/")
nested = re.sub(r"(?<![./])img/", "../img/", nested)
nested = re.sub(r"(?<![./])fonts/", "../fonts/", nested)
external_dir = ROOT / "external"
external_dir.mkdir(parents=True, exist_ok=True)
(external_dir / "index.html").write_text(nested, encoding="utf-8")

# Embed all referenced local images and fonts in the single-file deliverable.
paths = set(re.findall(r"(?:img|fonts)/[A-Za-z0-9_./-]+\.(?:webp|png|jpe?g|woff2)", source))
standalone = source
for rel in sorted(paths):
    file = ROOT / rel
    if not file.is_file():
        raise FileNotFoundError(f"Referenced asset does not exist: {file}")
    mime = mimetypes.guess_type(file.name)[0] or ("font/woff2" if file.suffix == ".woff2" else "application/octet-stream")
    data_uri = f"data:{mime};base64,{base64.b64encode(file.read_bytes()).decode('ascii')}"
    # Catalog data uses './img/...'; replace that entire prefix so no './data:' remains.
    standalone = standalone.replace("./" + rel, data_uri)
    standalone = standalone.replace(rel, data_uri)
# Without external WebP files, the standalone catalog uses its embedded PNGs.
standalone = standalone.replace("const USE_WEBP = true;", "const USE_WEBP = false;")
(ROOT / "index.html").write_text(standalone, encoding="utf-8")

# Build a lean deployment package: explicitly referenced files plus WebP companions
# selected at runtime by webpFor() for catalog/category PNG and JPEG sources.
package = ROOT / "netlify-package"
for name in ("img", "fonts"):
    target = package / name
    if target.exists():
        shutil.rmtree(target)
    target.mkdir(parents=True, exist_ok=True)
needed = set(paths)
for rel in list(paths):
    p = Path(rel)
    if p.parts[0] == "img" and p.suffix.lower() in (".png", ".jpg", ".jpeg"):
        webp_rel = p.with_suffix(".webp").as_posix()
        if (ROOT / webp_rel).is_file():
            needed.add(webp_rel)
for rel in sorted(needed):
    src = ROOT / rel
    dst = package / rel
    if not src.is_file():
        raise FileNotFoundError(f"Deployment asset does not exist: {src}")
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
shutil.copy2(ROOT / "favicon.png", package / "favicon.png")
shutil.copy2(ROOT / "og.jpg", package / "og.jpg")
shutil.copy2(ROOT / "netlify.toml", package / "netlify.toml")
shutil.copy2(SOURCE, package / "index.html")

# Refresh the two handoff archives; Netlify keeps its package contents at ZIP root.
with zipfile.ZipFile(ROOT / "ingrid-beauty-single-file.zip", "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
    zf.write(ROOT / "index.html", "index.html")
with zipfile.ZipFile(ROOT / "ingrid-beauty-netlify.zip", "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
    for file in sorted(package.rglob("*")):
        if file.is_file():
            zf.write(file, file.relative_to(package).as_posix())
print(f"Embedded {len(paths)} referenced local assets/fonts; deployment includes {len(needed)} image/font files")
print(f"standalone: {(ROOT / 'index.html').stat().st_size:,} bytes")
print(f"external: {SOURCE.stat().st_size:,} bytes")
print(f"netlify zip: {(ROOT / 'ingrid-beauty-netlify.zip').stat().st_size:,} bytes")
print(f"single-file zip: {(ROOT / 'ingrid-beauty-single-file.zip').stat().st_size:,} bytes")
