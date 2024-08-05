rm -rf dist
pip uninstall pyprojinit -y
python -m build
pip install -e .