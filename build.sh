rm -rf dist
pip uninstall tomifier -y
python -m build
pip install -e .