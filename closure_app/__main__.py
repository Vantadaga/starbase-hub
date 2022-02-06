from rich.console import Console
from rich.table import Table
import requests
import sys

def main():
    response = requests.get('https://api.bunnyslippers.dev/closures/')

    json = response.json()

    table = Table(title="Current Starbase Closures")

    table.add_column("Type", justify="right", style="cyan", no_wrap=True)
    table.add_column("Date", style="cyan")
    table.add_column("Time (CST)", style="cyan")
    table.add_column("Status", justify="right", style="cyan")

    for i in range(len(json)):
        table.add_row(json[i]['type'], json[i]['date'], json[i]['time'], json[i]['status'])

    console = Console()
    console.print(table)

if __name__ == "__main__":
    main()
