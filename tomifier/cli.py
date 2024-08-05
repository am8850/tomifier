import click
from .initcmd import init


@click.group()
def cli():
    click.echo(click.style("tomifier CLI", fg='yellow', bold=True))


cli.add_command(init)


def main():
    cli()


if __name__ == '__main__':
    main()
