import os
import click
import requests

from tomifier.fileutils import write_text


def create_folder_for_file(file: str) -> None:
    """
    Create a folder for the file
        :param file: The file
    """
    folder = file.split('/')
    if len(folder) > 1:
        folder = '/'.join(folder[:-1])
        if not folder:
            return
        if not os.path.exists(folder):
            os.makedirs(folder, exist_ok=True)


@click.command(help='Add a just a file or one from Ollama chat model generate code')
@click.option('-f', '--file', default='', help='The file name')
@click.option('-p', '--prompt', default='', help='Code Python generation prompt')
@click.option('-e', '--endpoint', default='http://localhost:11434/v1/chat/completions', help='The Ollama endpoint')
@click.option('-m', '--model', default='llama3', help='Ollama Chat model')
def add(file: str, prompt: str, endpoint: str, model: str) -> None:
    if file:
        click.echo(click.style(f"File: {file} added", fg='yellow'))
        create_folder_for_file(file)
        write_text(file, '')
        if model and prompt:
            try:
                data = {
                    "model": model,
                    "messages": [
                        {
                            "role": "system",
                            "content": "You are an expert Python AI coder. Generate the best code possible. Provide comments in the code. Just generate the code with no prologue."
                        },
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    "temperature": 0.1
                }
                resp = requests.post(endpoint, json=data, headers={
                                     'Content-Type': 'application/json', 'api-key': 'ollama'})
                resp.raise_for_status()
                code: str = resp.json()['choices'][0]['message']['content']
                if code:
                    code = code.replace('```', '').replace(
                        '```python', '').strip()
                    click.echo(click.style(f"Code generated.", fg='green'))
                    # click.echo(code)
                    write_text(file, code)
                else:
                    raise Exception("")
            except requests.exceptions.HTTPError as e:
                click.echo(click.style(
                    f"Unable to generate code {e}", fg='red'))
            except Exception as e:
                click.echo(click.style(
                    f"Unable to generate code {e}", fg='red'))
