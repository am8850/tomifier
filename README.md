# tomifier

`pyproject.toml` is a modern configuration file to package and publish Python packages. `tomifier` is a command-line tool to help you initialize a simple Python project. This is similar to the way  you can initialize a package in npm with `npm init`. The starter code itsef is a command-line interface (CLI) that can launch a FastAPI application and it comes with all the settings and tools to package and publish the generated code as a package.

If you have Ollama installed, `tomifier` now also offers code generation capabilities. You can use it to create new files in your project and/or generate code based on a prompt (see the `add` command usage details below).

References:
- [pyproject.toml vs setup.py](https://packaging.python.org/en/latest/guides/modernize-setup-py-project/)

## Installation

`pip install tomifier`

## Usage

Initialize a package in current Folder:
- `tomifier init`

Initialize a package at a target folder: 
- `tomifier init -o target_folder/`

Initialize a package with a given package name and at a target folder: 
- `tomifier init --name my-package1 --output target_folder/`

Add a file:
- `tomifier add -f myproject1/services/service1.py`

Add a file and generate Ollama code:
- `tomifier add -f myproject1/services/service1.py -p "write a function to add two integers"`

Sample output of creating a file and generating code:

```text
File: myproject1/service1.py added
code generated
```

## Sample run

This is what a sample `tomifier` run looks like:


```text
tomifier CLI
Description [My package]: Description for myproject1
Author [Name]: 
Author email [name@email.com]: 
Homepage [https://github.com/<usernane>/<repo>]: 
The following packages will be added by default: click, fastapi, and uvicorn[standard]
Command separated list of additional packages [ ]: 
Ready to inialize project. Proceed [Y/n]: 
Creating package: my-project1
Creating folder test1
New project iniatialized at: test1
Type: cd test1
 - Review the generated code
 - Check the package requirements in pyproject.toml and requirements.txt
 - To build the project type: sh.build
```

> **Note:** if you intend to deploy the package to pypi.org, make sure that the name is available. Even if it is available, the name could be too close to another name preventing posting. If you end up having to choose a different name, you will need to rename the package directory and the package name references in the `README.md`,`pyproject.toml` and `MANIFIST.in` files

## Scaffolded files

The CLI will scaffold the following files and folder structure at the current folder or at the given target folder:

```text
.
├── .devcontainer
│   └── devcontainer.json
├── .github
│   └── dependabot.yml
├── .gitignore
├── LICENSE
├── MANIFEST.in
├── README.md
├── build.sh
├── myproject1
│   ├── __init__.py
│   ├── cmd
│   │   ├── __init__.py
│   │   ├── root.py
│   │   └── static
│   │       └── index.html
│   └── version.py
├── pyproject.toml
├── requirements.txt
└── setup.py
```

The scaffolded files include:
- The project files
- The project publishing files including: `pyproject.toml, setup.py, MANIFEST.in, LICENSE, build.sh, and README.md`
- The `devcontainer` and `dependabot` folders and files for VS Code
- A `.gitignore` file

## Sample generated `pyproject.toml` file

```toml
[build-system]
requires = ["setuptools", "setuptools-scm"]
build-backend = "setuptools.build_meta"

[project]
name = "my-package1"
authors = [
  { name="Name", email="name@email.com" },
]
description = "Description my-package1"
readme = "README.md"
license = { file="LICENSE" }
requires-python = ">=3.9"
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]
dependencies = [
  "click",
  "fastapi",
  "uvicorn[standard]"
]
dynamic = ["version"]

[tool.setuptools]
include-package-data = true

[tool.setuptools.dynamic]
version = {attr = "mypackage1.version.VERSION"}
readme = {file = ["README.md"]}

[tool.setuptools.packages.find]
include = ["mypackage1*"]
exclude = ["*.tests*"]
namespaces = false

[tool.setuptools.package-data]
"mypackage1" = ["*.*"]

[project.urls]
"Homepage" = "https://github.com/<usernane>/<repo>"

[project.scripts]
mypackage1 = "mypackage1.cmd.root:main"
```

> **Note:** the `pyproject.toml` contents of this file can be and most likely will need to be modified further to meet your needs.

## Building the package

`build.sh` is a useful bash script included as part of the scaffolded code to build and deploy the package locally in editable mode. 

To run it from a bash terminal type: 

```bash
sh build.sh
```

The bash script includes the following commands:

```bash
rm -rf dist
pip uninstall mypackage1 -y
python -m build
pip install -e .
mypackage1 ui
```

## Pushing the package to pypi.org

After building the package, to push the build to pypi.org using twine. Type: 

```bash
# Verfify that the package name does not exist
# Install twine
pip install twine
# Make sure to get and install pypi.org token
# Publish the package
twine upload dis/*
```
