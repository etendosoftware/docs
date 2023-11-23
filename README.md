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

# Publish new version

```bash
source venv/bin/activate
mkdocs gh-deploy 

#After running `mkdocs gh-deploy`  make sure the action is finished in GitHub before running the following command: 

mike deploy --push --update-aliases 23.x latest

# mike set-default --push latest
```
x