import os
import re


def package_name_validator(s: str) -> bool:
    pattern = r"^[a-zA-Z][a-zA-Z0-9_-]*$"
    if re.match(pattern, s):
        return True
    return False


def file_exits_validator(output: str, name: str) -> bool:
    return os.path.isfile(f'{output}/LICENSE') \
        and os.path.isfile(f'{output}/README.md') \
        and os.path.isfile(f'{output}/setup.py') \
        and os.path.isfile(f'{output}/build.sh') \
        and os.path.isfile(f'{output}/MANIFEST.in') \
        and os.path.isfile(f'{output}/pyproject.toml') \
        and os.path.isfile(f'{output}/requirements.txt') \
        and os.path.isfile(f'{output}/.gitignore') \
        and os.path.isfile(f'{output}/{name}/__init__.py') \
        and os.path.isfile(f'{output}/{name}/version.py') \
        and os.path.isfile(f'{output}/{name}/cmd/__init__.py') \
        and os.path.isfile(f'{output}/{name}/cmd/root.py') \
        and os.path.isfile(f'{output}/{name}/cmd/static/index.html')
