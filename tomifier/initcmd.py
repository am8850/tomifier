import click
import os
import shutil

from .defaults import *
from .fileutils import write_bytes, write_text
from .validation import package_name_validator, file_exits_validator

def __list_str(packages: list) -> str:
    """
    Convert a list of packages to a string
        :param packages: The list of packages
        :return: The string of packages
    """
    deps = ''
    if packages.strip() != '':
        dep_list = packages.split(',')
        for i in range(len(dep_list)):
            dep = dep_list[i].strip()
            if dep != 'etc.':
                dep = dep_list[i].strip()
                deps += f'  "{dep}",\n'
        # delete the last comma
        deps = deps[:-2] + '\n'
    return deps

def __process(package_name: str,output_folder: str,required_packages: list,author: str,email:str,homepage:str,description:str) -> None:
    """
    Process the package creation
        :param package_name: The package name
        :param output_folder: The output folder
        :param required_packages: The required packages
        :param author: The author
        :param email: The email
        :param homepage: The homepage
        :param description: The description    
    """
    click.echo(f'Creating package: {package_name}')    
    if output_folder:
        # Create folder
        if output_folder!="." and not os.path.exists(output_folder):
            click.echo(f'Creating folder {output_folder}')
            os.makedirs(output_folder, exist_ok=True)        
        
        # # Create file from text
        write_bytes(f'{output_folder}/LICENSE', LICENSE_TXT)
        write_bytes(f'{output_folder}/README.md', README_MD)
        write_bytes(f'{output_folder}/MANIFEST.in', MANIFEST.replace("<name>", package_name))
        write_bytes(f'{output_folder}/setup.py', SETUP_PY)
        write_bytes(f'{output_folder}/build.sh', BUILD_SCRIPT.replace("<name>", package_name))
        
        dependencies = __list_str(required_packages)
        proj_toml= PYPROJECT.replace("<name>", package_name).replace("<author>", author).replace("<email>", email).replace("<DEPS>", dependencies).replace("<home_page>", homepage).replace("<description>", description)
        write_bytes(f'{output_folder}/pyproject.toml', proj_toml)        

        # Create the project files        
        os.makedirs(f'{output_folder}/{package_name}', exist_ok=True)
        write_text(f'{output_folder}/{package_name}/__init__.py','')
        write_bytes(f'{output_folder}/{package_name}/version.py', VERSION_PY)

        os.makedirs(f'{output_folder}/{package_name}/cmd', exist_ok=True)
        write_bytes(f'{output_folder}/{package_name}/cmd/__init__.py',INIT_PY)
        write_bytes(f'{output_folder}/{package_name}/cmd/root.py', ROOT_PY.replace("<name>", package_name))

        os.makedirs(f'{output_folder}/{package_name}/cmd/static', exist_ok=True)
        write_bytes(f'{output_folder}/{package_name}/cmd/static/index.html', INDEX_HTML)
                
        # report creation
        validation = file_exits_validator(output_folder,package_name)
        if validation:
            if output_folder != ".":
                click.echo(f"New project iniatialized at: {output_folder}")
            else:
                click.echo("New project inialized")
        else:
            click.echo("unable to initialize the project")
            if output_folder != ".":
                try:
                    shutil.rmtree(output_folder)   
                except:
                    click.echo(f"Unable to delete the folder: {output_folder}")


@click.command()
@click.option('-n','--name', default='', help='Package name')
@click.option('-o','--output', default='.', help='Target folder')
def init(name: str, output: str):    
    if not name:
        name = click.prompt('Package name',default='mypackage')    
    if not package_name_validator(name):
        click.echo(f"The package name '{name}' is invalid. A valid package name start with a letter, can have numbers, dashes, and underscores.")
        exit(1)        

    description = click.prompt('Description', default='My package')
    author = click.prompt('Author', default='Name')
    email = click.prompt('Author email', default='name@email.com')
    homepage = click.prompt('Homepage', default='https://github/usernane/repo')
    packages = click.prompt('Comma separated packages (space=None)', default='click, fastapi, unvicorn[standard]')    

    confirm = click.confirm("Ready to inialize project. Proceed",default=True)
    if not confirm:
        click.echo("Project creation cancelled")
        exit(0)

    __process(package_name=name,
            output_folder=output,
            required_packages=packages,
            author=author,
            email=email,
            homepage=homepage,
            description=description)                    