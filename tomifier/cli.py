
import click
from tomifier.addcmd import add
from tomifier.fileutils import write_text
from tomifier.initcmd import init


@click.group()
def cli():
    click.echo(click.style("tomifier CLI", fg='yellow', bold=True))


cli.add_command(init)
cli.add_command(add)


def main():
    add()
    # cli()


if __name__ == '__main__':
    # add()
    main()
