# tomifier

`pyproject.toml` is a modern way to create a python package. `tomifier` is CLI to initialize a simple Python pyproject.toml file and starting code. The starting code is itself a CLI that can launch a web application.

References:
[pyproject.toml vs setup.py](https://packaging.python.org/en/latest/guides/modernize-setup-py-project/)

## Installation

`pip install tomifier`

## Usage

Initialize on current Folder:
- `tomifier init`

Initialize on target folder: 
- `tomifier init -o target_folder/`

Initialize with a project name and a target folder: 
- `tomifier init --name myproject1 --output target_folder/`

## Files created

The CLI will create the following files and folder structure locally or at the target folder:

```text
LICENSE
README
pyproject.toml
MANIFEST.in
setup.py
buid.sh
<package_name>/__init__.py
<package_name>/version.py
<package_name>/cmd/__init__.py
<package_name>/cmd/root.py
<package_name>/cmd/static/index.html
```

## Sample Output from running the tool

```text
 tomifier init --output myproj1
tomifier CLI
Package name [mypackage]: myproject1
Description [My package]: Description for myproject1
Author [Name]: 
Author email [name@email.com]: 
Homepage [https://github/usernane/repo]: 
Comma separated packages (space=None) [click, fastapi, unvicorn[standard]]: 
Creating package myproject1 in folder myproj1 with author Name and email name@email.com
Creating folder myproj1
New project iniatialize at: myproj1
```

## Sample generated `pyproject.toml` file

```toml
[build-system]
requires = ["setuptools", "setuptools-scm"]
build-backend = "setuptools.build_meta"

[project]
name = "myproject1"
authors = [
  { name="Name", email="name@email.com" },
]
description = "Description for myproject1"
readme = "README.md"
license = { file="LICENSE" }
requires-python = ">=3.10, <3.12"
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]

dependencies = [
  "click",
  "fastapi",
  "unvicorn[standard]"
]

dynamic = ["version"]

[tool.setuptools]
include-package-data = true

[tool.setuptools.dynamic]
version = {attr = "myproject1.version.VERSION"}
readme = {file = ["README.md"]}

[tool.setuptools.packages.find]
include = ["myproject1*"]
exclude = ["*.tests*"]
namespaces = false

[tool.setuptools.package-data]
"myproject1" = ["*.*"]

[project.urls]
"Homepage" = "https://github/usernane/repo"

[project.scripts]
myproject1 = "myproject1.cmd.root:main"
```

## `build.sh`

`build.sh` is a useful bash script to start the build process and deploy the package locally in editable mode.