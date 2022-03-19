import click
from .checkout_and_pull import chpl
from .checkout import ch
from .add_all_and_commit import aac
from .add_single_file import a

@click.group()
def cli():
    pass    

cli.add_command(ch)
cli.add_command(chpl)
cli.add_command(aac)
cli.add_command(a)

if __name__ == '__main__':
    cli()