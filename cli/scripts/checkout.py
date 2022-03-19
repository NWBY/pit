import click
import subprocess

@click.command()
@click.argument('branch')
@click.option('-c', '--create', default=False, type=bool)
def ch(branch, create):
    if create:
        cmd = subprocess.Popen(['git', 'checkout', '-b', branch], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    else:
        cmd = subprocess.Popen(['git', 'checkout', branch], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
    stdout, stderr = cmd.communicate()
    
    click.echo(f'Checked out {branch} bad boy')