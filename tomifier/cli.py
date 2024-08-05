import os
import click
from .defaults import *

def write_text(file_path: str, content: str):    
    with open(f'{file_path}', 'w') as f:
        f.write(content)

def write_bytes(file_path: str, content: str):
    bytes = str.encode(content)
    with open(f'{file_path}', 'wb') as f:
        f.write(bytes)

@click.group()
def cli():
    click.echo("tomifier CLI")

@cli.command()
@click.option('--name', default='', help='Package name')
@click.option('--output', default='.', help='Installation folder')
def init(name: str, output: str):
    if not name:
        name = click.prompt('Package name',default='mypackage')
    description = click.prompt('Description', default='My package')
    author = click.prompt('Author', default='Name')
    email = click.prompt('Author email', default='name@email.com')
    homepage = click.prompt('Homepage', default='https://github/usernane/repo')
    packages = click.prompt('Comma separated packages (space=None)', default='click, fastapi, unvicorn[standard]')
    
    click.echo(f'Creating package {name} in folder {output} with author {author} and email {email}')
    
    if output:
        # Create folder
        if output!=".":
            click.echo(f'Creating folder {output}')
            os.makedirs(output, exist_ok=True)
        # # Create file from text
        write_bytes(f'{output}/LICENSE', LICENSE_TXT)
        write_bytes(f'{output}/README.md', README_MD)
        #write_bytes(f'{output}/MANIFEST.in', defaults.MANIFEST.replace("<name>", name))
        write_bytes(f'{output}/setup.py', 'from setuptools import setup\nsetup()')
        write_bytes(f'{output}/build.sh', BUILD_SCRIPT.replace("<name>", name))

        deps = ''
        if packages.strip() != '':
            deps = ''
            dep_list = packages.split(',')
            for i in range(len(dep_list)):
                dep = dep_list[i].strip()
                if dep != 'etc.':
                    dep = dep_list[i].strip()
                    deps += f'  "{dep}",\n'
            deps = deps[:-2] + '\n'
                
        proj_toml= PYPROJECT.replace("<name>", name).replace("<author>", author).replace("<email>", email).replace("<DEPS>", deps).replace("<home_page>", homepage).replace("<description>", description)
        write_bytes(f'{output}/pyproject.toml', proj_toml)        

        # Create the project files        
        os.makedirs(f'{output}/{name}', exist_ok=True)
        write_text(f'{output}/{name}/__init__.py','')
        write_bytes(f'{output}/{name}/version.py', VERSION_PY)

        os.makedirs(f'{output}/{name}/cmd', exist_ok=True)
        write_text(f'{output}/{name}/cmd/__init__.py','from .root import *')
        write_bytes(f'{output}/{name}/cmd/root.py', ROOT_PY)

        # report creation
        if output != ".":
            click.echo(f"New project iniatialized at: {output}")
        else:
            click.echo("New project inialized")

def main():
    cli()

if __name__ == '__main__':
    main()