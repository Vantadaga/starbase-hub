from rich.console import Console
from rich.table import Table
import requests
import sys

def main():
    closure_response = requests.get('https://api.bunnyslippers.dev/closures/')
    tfr_response = requests.get('https://api.bunnyslippers.dev/tfrs/')

    closure_json = closure_response.json()
    tfr_json = tfr_response.json()

    closures = Table(title="Current Starbase Closures")

    closures.add_column("Type", justify="right", style="cyan", no_wrap=True)
    closures.add_column("Date", style="cyan")
    closures.add_column("Time (CST)", style="cyan")
    closures.add_column("Status", justify="right", style="cyan")

    for i in range(len(closure_json)):
        closures.add_row(closure_json[i]['type'], closure_json[i]['date'], closure_json[i]['time'], closure_json[i]['status'])

    tfrs = Table(title="Current Starbase Temporary Flight Restrictions (TFR)")

    tfrs.add_column("Notam Number", justify="right", style="cyan", no_wrap=True)
    tfrs.add_column("Issue Date", style="cyan")
    tfrs.add_column("Start Date", style="cyan")
    tfrs.add_column("End Date", style="cyan")
    tfrs.add_column("Altitude", justify="right", style="cyan")

    for i in range(len(tfr_json)):
        tfrs.add_row(tfr_json[i]['notamNumber'], tfr_json[i]['issueDate'], tfr_json[i]['startDate'], tfr_json[i]['endDate'], tfr_json[i]['altitude'])


    console = Console()
    console.print(closures)
    console.print(tfrs)

if __name__ == "__main__":
    main()
