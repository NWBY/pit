import click
import subprocess

@click.command()
@click.argument('file', nargs=-1)
def a(file):
    file_string = ' '.join(file)
    
    cmd = subprocess.Popen(['git', 'add', file_string], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    stdout, stderr = cmd.communicate()
    
    click.echo(f'Added all these files bad boy: {file_string}')
    
