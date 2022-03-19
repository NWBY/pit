import click
from .checkout_and_pull import chpl
from .checkout import ch

@click.group()
def cli():
    pass    

cli.add_command(ch)
cli.add_command(chpl)

if __name__ == '__main__':
    cli()