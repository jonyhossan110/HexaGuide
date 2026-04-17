import os
import sys
from datetime import datetime

from hexaguide.cli import get_args
from hexaguide.engine import build_workflow
from hexaguide.formatter import console, print_banner, print_section, print_footer
from hexaguide import __version__

REPORTS_DIR = "reports"


def _sanitize(target: str) -> str:
    return target.replace("/", "_").replace(":", "_").replace("*", "_")


def _save_report(target: str, workflow: list[dict]) -> str:
    os.makedirs(REPORTS_DIR, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = os.path.join(REPORTS_DIR, f"{_sanitize(target)}_{stamp}.txt")

    sep  = "=" * 62
    dash = "-" * 52

    lines = [
        sep,
        f"  HEXAGUIDE v{__version__} — PENTEST REPORT",
        f"  Target    : {target}",
        f"  Generated : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"  By        : HexaCyberLab (hexacyberlab.com)",
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
        "  LEGAL: Use only on systems you have written permission to test.",
        "  Unauthorized access is illegal. HexaCyberLab bears no responsibility.",
        sep,
    ]

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    return path


def main():
    args = get_args()

    target = (
        args.target.strip()
        .replace("https://", "")
        .replace("http://", "")
        .rstrip("/")
    )

    section_filter = getattr(args, "section", None)

    try:
        workflow = build_workflow(target, section_filter=section_filter)
    except FileNotFoundError:
        console.print("[bold red]✘[/bold red] commands.json not found — reinstall HexaGuide.")
        sys.exit(1)
    except ValueError as e:
        console.print(f"[bold red]✘[/bold red] {e}")
        sys.exit(1)
    except Exception as e:
        console.print(f"[bold red]✘ Unexpected error:[/bold red] {e}")
        sys.exit(1)

    print_banner(target)

    for section in workflow:
        print_section(section)

    if not args.no_save:
        report_path = _save_report(target, workflow)
        print_footer(report_path)
    else:
        console.print("\n[dim]  Report saving skipped (--no-save flag)[/dim]\n")


if __name__ == "__main__":
    main()
