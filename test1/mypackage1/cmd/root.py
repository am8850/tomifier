import click
import fastapi
from fastapi.staticfiles import StaticFiles
import uvicorn
import os

@click.group()
def cli():
    click.echo("mypackage1 CLI")

@cli.command()
def ui():
    app = fastapi.FastAPI()
    
    @app.get('/api/status')
    def read_root():
        return {'status': 'healthy'}
    
    local_folder = os.path.dirname(os.path.abspath(__file__))
    static_foler = os.path.join(local_folder, 'static')
    print(static_foler)
    app.mount("/", StaticFiles(directory=static_foler,html = True), name="static")

    uvicorn.run(app)

def main():
    cli()

if __name__ == "__main__":
    main()
