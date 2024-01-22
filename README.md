# First Install

```bash
python3 -m venv venv
source venv/bin/activate
pip install mkdocs-material
pip install pillow cairosvg
pip install mkdocs-glightbox
pip install mike
pip install mkdocs-rss-plugin
```

# Run Etendo Documentation locally

```bash
source venv/bin/activate
mike serve
# mkdocs serve
```


## When a new version of mike is released, it is necessary to update the latest reference manually.
```bash
mike set-default --push latest
```