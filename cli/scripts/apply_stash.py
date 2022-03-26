import click
import subprocess

@click.command()
@click.argument('stash_index')
def sa(stash_index):
    stdout, stderr = subprocess.Popen([], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    click.echo('Applied stash bad boy')
