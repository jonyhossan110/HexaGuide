from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.rule import Rule
from rich import box
from rich.padding import Padding
from rich.columns import Columns
from hexaguide import __version__

console = Console()

BANNER = r"""
  _   _                   ____       _     _
 | | | | _____  ____ _   / ___|_   _(_) __| | ___
 | |_| |/ _ \ \/ / _` | | |  _| | | | |/ _` |/ _ \
 |  _  |  __/>  < (_| | | |_| | |_| | | (_| |  __/
 |_| |_|\___/_/\_\__,_|  \____|\__,_|_|\__,_|\___|
"""


def print_banner(target: str) -> None:
    console.print(f"[bold red]{BANNER}[/bold red]")

    info = Table.grid(padding=(0, 2))
    info.add_column(style="bold cyan",  no_wrap=True)
    info.add_column(style="white")
    info.add_row("Target",  f"[bold green]{target}[/bold green]")
    info.add_row("Version", f"[dim]v{__version__}[/dim]")
    info.add_row("Author",  "[bold cyan]Md. Jony Hassain[/bold cyan] — HexaCyberLab")
    info.add_row("Website", "[link=https://hexacyberlab.com][dim]hexacyberlab.com[/dim][/link]")

    console.print(
        Panel(
            info,
            title="[bold red]⬡ HexaGuide Pentest Report[/bold red]",
            border_style="red",
            expand=False,
            padding=(1, 3),
        )
    )
    console.print()

    # Legal warning
    console.print(
        Panel(
            "[bold yellow]⚠  WARNING:[/bold yellow] [dim]Use only on systems you own or have "
            "explicit written permission to test.\n"
            "   Unauthorized access is illegal. HexaCyberLab bears no responsibility for misuse.[/dim]",
            border_style="yellow",
            padding=(0, 2),
        )
    )
    console.print()


def print_section(section: dict) -> None:
    console.print(
        Rule(
            f"[bold yellow] [{section['number']}]  {section['title']} [/bold yellow]",
            style="yellow",
            align="left",
        )
    )
    console.print()

    for idx, entry in enumerate(section["tools"], 1):
        tbl = Table(
            box=box.ROUNDED,
            show_header=False,
            padding=(0, 1),
            expand=False,
            border_style="dim white",
            min_width=70,
        )
        tbl.add_column("Key",   style="bold cyan",  no_wrap=True, width=11)
        tbl.add_column("Value", style="white",       no_wrap=False)

        tbl.add_row("Tool",    f"[bold magenta]{entry['tool']}[/bold magenta]")
        tbl.add_row("Command", f"[bold green]{entry['cmd']}[/bold green]")
        tbl.add_row("Purpose", f"[dim]{entry['desc']}[/dim]")

        console.print(Padding(tbl, (0, 4)))
        console.print()

    console.print()


def print_footer(report_path: str) -> None:
    grid = Table.grid(padding=(0, 2))
    grid.add_column(style="bold cyan", no_wrap=True)
    grid.add_column(style="white")
    grid.add_row("Report", f"[bold green]{report_path}[/bold green]")
    grid.add_row("Tip",    "[dim]All commands are copy-ready. Adjust wordlist paths as needed.[/dim]")
    grid.add_row("Agency", "[dim]HexaCyberLab — hexacyberlab.com[/dim]")

    console.print(
        Panel(
            grid,
            title="[bold green]✔  Scan Complete[/bold green]",
            border_style="green",
            padding=(1, 3),
        )
    )
    console.print()
