"""main.py — Entry point for HexaGuide CLI."""
import os
import sys
from datetime import datetime

from hexaguide import __version__
from hexaguide.cli import get_args
from hexaguide.engine import build_workflow
from hexaguide.formatter import console, print_banner, print_section, print_footer

REPORTS_DIR = "reports"


def _sanitize(target: str) -> str:
    """Remove characters that are unsafe in filenames."""
    for ch in ("/", "\\", ":", "*", "?", '"', "<", ">", "|"):
        target = target.replace(ch, "_")
    return target


def _save_report(target: str, workflow: list[dict]) -> str:
    """Save a plain-text copy of the workflow to reports/<target>_<timestamp>.txt."""
    os.makedirs(REPORTS_DIR, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{_sanitize(target)}_{stamp}.txt"
    path = os.path.join(REPORTS_DIR, filename)

    sep  = "=" * 62
    dash = "-" * 52
    now  = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    lines = [
        sep,
        f"  HEXAGUIDE v{__version__} — WEB PENTEST REPORT",
        f"  Target    : {target}",
        f"  Generated : {now}",
        f"  By        : Md. Jony Hassain — HexaCyberLab (hexacyberlab.com)",
        sep,
        "",
    ]

    for section in workflow:
        lines += [
            f"[{section['number']}] {section['title'].upper()}",
            dash,
        ]
        for entry in section["tools"]:
            lines += [
                f"  Tool    : {entry['tool']}",
                f"  Command : {entry['cmd']}",
                f"  Purpose : {entry['desc']}",
                "",
            ]
        lines.append("")

    lines += [
        sep,
        "  LEGAL NOTICE:",
        "  Use ONLY on systems you own or have explicit written permission to test.",
        "  Unauthorized access is illegal. HexaCyberLab bears no responsibility.",
        sep,
        "",
    ]

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    return path


def main() -> None:
    args = get_args()

    # Strip protocol prefix — keep domain/IP only
    target = (
        args.target.strip()
        .replace("https://", "")
        .replace("http://", "")
        .rstrip("/")
    )

    try:
        workflow = build_workflow(target, section_filter=args.section)
    except FileNotFoundError:
        console.print(
            "[bold red]✘[/bold red] commands.json not found.\n"
            "  Try reinstalling: [cyan]pip install --force-reinstall .[/cyan]"
        )
        sys.exit(1)
    except ValueError as exc:
        console.print(f"[bold red]✘[/bold red] {exc}")
        sys.exit(1)
    except Exception as exc:
        console.print(f"[bold red]✘ Unexpected error:[/bold red] {exc}")
        sys.exit(1)

    print_banner(target)

    for section in workflow:
        print_section(section)

    if not args.no_save:
        report_path = _save_report(target, workflow)
        print_footer(report_path)
    else:
        console.print("\n[dim]  Report saving skipped (--no-save)[/dim]\n")


if __name__ == "__main__":
    main()
