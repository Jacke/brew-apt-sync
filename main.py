from rich import print
from yaml import load, dump
import pprint
import time
import typer
from tqdm import tqdm
from typing import (
    List
)


pp = pprint.PrettyPrinter(indent=4)

pp.pprint('hello')
print("Hello, [bold magenta]World[/bold magenta]!", ":vampire:", locals())

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

# ...
try:
    with open('./test_packages.yaml', 'r') as file:
      # correct_tag = file.read().strip()
      data = load(file, Loader=Loader)

      for value in data['packages']:
        print('->', value)

      output = dump(data, Dumper=Dumper)
      pp.pprint(output)
finally:
  pp.pprint('done')

from rich.console import Console
from rich.table import Table

console = Console()

table = Table(show_header=True, header_style="bold magenta")
table.add_column("Date", style="dim", width=12)
table.add_column("Title")
table.add_column("Production Budget", justify="right")
table.add_column("Box Office", justify="right")
table.add_row(
    "Dec 20, 2019", "Star Wars: The Rise of Skywalker", "$275,000,000", "$375,126,118"
)
table.add_row(
    "May 25, 2018",
    "[red]Solo[/red]: A Star Wars Story",
    "$275,000,000",
    "$393,151,347",
)
table.add_row(
    "Dec 15, 2017",
    "Star Wars Ep. VIII: The Last Jedi",
    "$262,000,000",
    "[bold]$1,332,539,889[/bold]",
)

console.print(table)

app = typer.Typer()

PACKAGES_STORE = "uni_packs.yaml"

for i in tqdm(range(10)):
  time.sleep(0.03)
  pass

ALL_PLATFORMS: List[str] = ["macos", "ubuntu"]

@app.command()
def scan():
    """
    Scan installed packages and write to packages store
    """
    # Run fetcher based on platform
    # Prepare list of packages
    # Wrote list of packages to yaml
    # If yaml exist then run DIFF
    # Overwrite (y/n)
    typer.echo("Scan")
    typer.echo("Package ...")
    typer.echo("Package ...")
    typer.echo("Package ...")
    number_of_packages = 100
    typer.echo(f"Found package {n} wrote to {PACKAGES_STORE}")

@app.command()
def list(
    yaml: bool = typer.Option(False, help="Output as YAML",)):
    """
    Show current packages table
    """
    #    Or view packages as YAML with [yq](https://github.com/mikefarah/yq):
    #    list --yaml | yq '.name'
    typer.echo("YAML viewer of uni_packs.yaml")

@app.command()
def package(container_name: str, platforms: List[str] = ALL_PLATFORMS):
    """
    Create zip archive with installer
    """
    # Get List of Packages
    # Create tmp folder
    # Add mapper (Packages -> Brewfile//Aptfile) for platform
    # Add script installer
    # Create zip -- upload to temp file storage -- show link
    typer.echo(f"Create {container_name}.zip for platforms: {platforms}")

if __name__ == "__main__":
    app()
