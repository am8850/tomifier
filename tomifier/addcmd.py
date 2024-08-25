import click
import requests

from tomifier.fileutils import write_text


@click.command(help='Add a just a file or one from Ollama chat model generate code')
@click.option('-f', '--file', default='test1/project1/test.py', help='File name')
@click.option('-p', '--prompt', default='Write a function to find the 1001st prime number', help='Code generation prompt')
@click.option('-e', '--endpoint', default='http://localhost:11434/v1/chat/completions', help='Ollama endpoint')
@click.option('-m', '--model', default='llama3', help='Ollama chat model')
def add(file: str, prompt: str, endpoint: str, model: str) -> None:
    if file:
        click.echo(click.style(f"File: {file} added", fg='yellow'))
        write_text(file, '')
        if model and prompt:
            try:
                print(prompt, model, endpoint)
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
                    click.echo(click.style(f"Code generated:", fg='green'))
                    click.echo(code)
                    write_text(file, code)
                else:
                    raise Exception("")
            except requests.exceptions.HTTPError as e:
                click.echo(click.style(
                    f"Unable to generate code {e}", fg='red'))
            except Exception as e:
                click.echo(click.style(
                    f"Unable to generate code {e}", fg='red'))
