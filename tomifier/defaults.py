LICENSE_TXT = "MIT License"
README_MD = "Update this README.md with instructions for your package"
MANIFEST = "include-recursive <name>/web/ui *"
PYPROJECT = '''[build-system]
requires = ["setuptools", "setuptools-scm"]
build-backend = "setuptools.build_meta"

[project]
name = "<name>"
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

BUILD_SCRIPT='''# Build and install the package locally
python -m build && pip install -e .

# Test the package
<name> ui
'''

ROOT_PY = '''import click
import fastapi
import uvicorn

@click.group()
@click.option('--debug/--no-debug', default=False)
def cli(debug):
    pass

@cli.command()
def ui():
    app = fastapi.FastAPI()
    @app.get('/')
    def read_root():
        return {'Hello': 'World'}
    uvicorn.run(app)

def main():
    cli()
'''

VERSION_PY ='''version="0.0.1"
__version__ = version
VERSION=version
'''