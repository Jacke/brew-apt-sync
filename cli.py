import typer

app = typer.Typer()
@app.command()
def scan(name: str):
    typer.echo(f"Scan packages {name}")

@app.command()
def generate(name: str, formal: bool = False):
    if formal:
        typer.echo(f"Goodbye Ms. {name}. Have a good day.")
    else:
        typer.echo(f"Bye {name}!")

@app.command()
def package(name: str, formal: bool = False):
    if formal:
        typer.echo(f"Goodbye Ms. {name}. Have a good day.")
    else:
        typer.echo(f"Bye {name}!")

if __name__ == "__main__":
    app()
