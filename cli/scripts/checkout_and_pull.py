from sys import stderr
import click
import subprocess

@click.command()
@click.argument('branch')
def chpl(branch):
    cmd = subprocess.Popen(['git', 'checkout', branch, '&&', 'git', 'pull'],
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
    stdout, stderr = cmd.communicate()
    
    click.echo(f'Checked out {branch} and pulled that bad boy')