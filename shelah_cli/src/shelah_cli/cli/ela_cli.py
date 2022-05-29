import click
import requests

import shelah_cli

@click.group() 
@click.version_option(message="Shelah CLI v" + shelah_cli.__version__)
def ela_cli():
    '''
    Shelah CLI command tool
    '''

@ela_cli.group()
def get():
    '''
    Asks Shelah to for a specific resource
    '''

@get.command()
def theories():
    '''
    Returns a list of first-order theories for which Shelah can generate models.
    '''
    SHELAH_GATEWAY_URL              = "localhost:8000"

    # r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
    response                        = requests.get("http://" + SHELAH_GATEWAY_URL + "/theories")

    response.status_code

    data                            = response.json()
    click.echo("Success")
    click.echo(data)

    #raise NotImplementedError