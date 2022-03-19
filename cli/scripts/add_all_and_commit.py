import click
import subprocess

@click.command()
@click.argument('message')
def aac(message):
    add_cmd = subprocess.Popen(['git', 'add', '.'], 
                           stdout=subprocess.PIPE, 
                           stderr=subprocess.PIPE)
    
    stdout, stderr = add_cmd.communicate()
    
    commit_cmd = subprocess.Popen(['git', 'commit', '-m', f'{message}'], 
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE)

    stdout, stderr = commit_cmd.communicate()
    
    click.echo(f'Added all and commited that bad boy message: {message}')
