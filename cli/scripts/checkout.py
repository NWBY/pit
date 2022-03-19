import click
import subprocess

@click.command()
@click.argument('branch')
def ch(branch):
    cmd = subprocess.Popen(['git', 'checkout', branch],
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
    stdout, stderr = cmd.communicate()
    
    click.echo(f'Checked out {branch} bad boy')