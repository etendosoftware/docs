# First Install

```bash
python3 -m venv venv
source venv/bin/activate
pip install mkdocs-material
pip install pillow cairosvg
pip install mkdocs-glightbox
pip install mike
```

# Run Etendo Documentation locally

```bash
source venv/bin/activate
mkdocs serve
```

# Publish new version

```bash
mkdocs gh-deploy --force
# mike deploy --push --update-aliases 23.x latest
# mike set-default --push latest
```
