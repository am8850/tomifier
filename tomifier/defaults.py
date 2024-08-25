LICENSE_TXT = '''MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

README_MD = '''# `<package_name>`

Update this files with instructions for your package.

## To run the package type:

`<name> ui`
'''

MANIFEST = '''include-recursive <name>/root/static *
'''

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
requires-python = ">=3.9"
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

BUILD_SCRIPT = '''rm -rf dist
pip uninstall <package_name> -y
python -m build
pip install -e .
<name> ui
'''

ROOT_PY = '''import click
import fastapi
from fastapi.staticfiles import StaticFiles
import uvicorn
import os

@click.group(help="<name> CLI")
def cli():
    click.echo("<name> CLI")

@cli.command(help="Start a fastapi server that serves both static and APIs")
@click.option("--port", default=8000, help="Port number")
@click.option("--host", default="127.0.0.1", help="Host address")
def ui(host:str, port:int):
    app = fastapi.FastAPI()
    
    @app.get('/api/status')
    def read_root():
        return {'status': 'healthy'}
    
    local_folder = os.path.dirname(os.path.abspath(__file__))
    static_foler = os.path.join(local_folder, 'static')
    print(static_foler)
    app.mount("/", StaticFiles(directory=static_foler,html = True), name="static")

    uvicorn.run(app, host=host, port=port)

if __name__ == "__main__":
    cli()
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

REQUIREMENTS_TXT = '''<DEPS>'''

GIT_IGNORE = '''__pycache__
*.egg-info
dist

.venv
.env
'''

DEV_CONTAINER_JSON = '''// For format details, see https://aka.ms/devcontainer.json. For config options, see the
// README at: https://github.com/devcontainers/templates/tree/main/src/python
{
	"name": "Python 3",
	// Or use a Dockerfile or Docker Compose file. More info: https://containers.dev/guide/dockerfile
	"image": "mcr.microsoft.com/devcontainers/python:1-3.11-bullseye",
	"features": {
		"ghcr.io/devcontainers/features/node:1": {}
	},
	// Features to add to the dev container. More info: https://containers.dev/features.
	// "features": {},
	// Use 'forwardPorts' to make a list of ports inside the container available locally.
	// "forwardPorts": [
	// 	8000
	// ],
	// Use 'postCreateCommand' to run commands after the container is created.
	// "postCreateCommand": "pip3 install --user -r requirements.txt",
	// Configure tool-specific properties.
	"customizations": {
		"vscode": {
			"extensions": [
				"ms-python.python",
				"ms-python.debugpy",
				"ms-toolsai.jupyter",
				"ms-toolsai.jupyter-keymap",
				"ms-toolsai.vscode-jupyter-slideshow",
				"ms-toolsai.jupyter-renderers",
				"ms-toolsai.vscode-jupyter-cell-tags",
				"otnettools.dotnet-interactive-vscode",
				"ms-python.autopep8"
			]
		}
	}
	// Uncomment to connect as root instead. More info: https://aka.ms/dev-containers-non-root.
	// "remoteUser": "root"
}
'''

DEPENDABOT_YML = '''# To get started with Dependabot version updates, you'll need to specify which
# package ecosystems to update and where the package manifests are located.
# Please see the documentation for more information:
# https://docs.github.com/github/administering-a-repository/configuration-options-for-dependency-updates
# https://containers.dev/guide/dependabot

version: 2
updates:
 - package-ecosystem: "devcontainers"
   directory: "/"
   schedule:
     interval: weekly
'''
