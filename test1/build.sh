rm -rf dist
pip uninstall my-package1 -y
python -m build
pip install -e .
mypackage1 ui
