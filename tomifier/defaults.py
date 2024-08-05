LICENSE_TXT = "MIT License"

README_MD = """# `<package_name>`

Update this files with instructions for your package.

## To run the package type:

`<name> ui`
"""

MANIFEST = """include-recursive <name>/root/static *
"""

PYPROJECT = '''[build-system]
requires = ["setuptools", "setuptools-scm"]
build-backend = "setuptools.build_meta"

[project]
name = "<package_name>"
authors = [
  { name="<author>", email="<email>" },
]
description = "<description>"
readme = "README.md"
license = { file="LICENSE" }
requires-python = ">=3.10, <3.12"
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]

dependencies = [
<DEPS>]

dynamic = ["version"]

[tool.setuptools]
include-package-data = true

[tool.setuptools.dynamic]
version = {attr = "<name>.version.VERSION"}
readme = {file = ["README.md"]}

[tool.setuptools.packages.find]
include = ["<name>*"]
exclude = ["*.tests*"]
namespaces = false

[tool.setuptools.package-data]
"<name>" = ["*.*"]

[project.urls]
"Homepage" = "<home_page>"

[project.scripts]
<name> = "<name>.cmd.root:main"
'''

BUILD_SCRIPT = '''# Build and install the package locally
python -m build && pip install -e .

# Test the package
<name> ui
'''

ROOT_PY = '''import click
import fastapi
from fastapi.staticfiles import StaticFiles
import uvicorn
import os

@click.group()
def cli():
    click.echo("mypackage CLI")

@cli.command()
def ui():
    app = fastapi.FastAPI()
    
    @app.get('/api/status')
    def read_root():
        return {'status': 'healthy'}
    
    local_folder = os.path.dirname(os.path.abspath(__file__))
    static_foler = os.path.join(local_folder, 'static')
    print(static_foler)
    app.mount("/", StaticFiles(directory=static_foler,html = True), name="static")

    uvicorn.run(app)

def main():
    cli()

if __name__ == "__main__":
    main()
'''

VERSION_PY = '''version="0.0.1"
__version__ = version
VERSION=version
'''

SETUP_PY = '''from setuptools import setup

setup()
'''

INIT_PY = '''from .root import *
'''

INDEX_HTML = '''<!DOCTYPE html>
<html>
<head>
    <title>Tomifier</title>
</head>
<body>
    <h1>Tomifier</h1>
    <p>Tomify your Python projects</p>
</body>
</html>
'''
