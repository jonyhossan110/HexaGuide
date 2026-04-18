"""
engine.py — Loads commands.json and builds the pentest workflow.

commands.json lives at hexaguide/data/commands.json (inside the package)
so it is always accessible after `pip install`, regardless of working directory.
"""
import json
import os

# Resolve path relative to THIS file — always correct after pip install
_HERE     = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(_HERE, "data", "commands.json")

SECTION_MAP = {
    "recon":     ("Reconnaissance",           "1"),
    "subdomain": ("Subdomain Enumeration",    "2"),
    "scan":      ("Scanning",                 "3"),
    "directory": ("Directory Bruteforce",     "4"),
    "vuln":      ("Vulnerability Scan",       "5"),
    "exploit":   ("Exploitation Suggestions", "6"),
    "auth":      ("Authentication Testing",   "7"),
    "ssl":       ("SSL Analysis",             "8"),
}

VALID_SECTIONS = list(SECTION_MAP.keys())


def load_commands() -> dict:
    """Load and return the raw commands dictionary from commands.json."""
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def build_workflow(target: str, section_filter: str | None = None) -> list[dict]:
    """
    Build the full pentest workflow for *target*.

    Args:
        target:         Domain or IP address (e.g. 'example.com').
        section_filter: If given, return only that one section.

    Returns:
        List of section dicts: {number, title, tools: [{tool, cmd, desc}]}

    Raises:
        FileNotFoundError: commands.json missing (corrupted install).
        ValueError:        Unknown section_filter key.
    """
    if section_filter and section_filter not in SECTION_MAP:
        raise ValueError(
            f"Unknown section '{section_filter}'. "
            f"Choose from: {', '.join(VALID_SECTIONS)}"
        )

    raw = load_commands()

    workflow = []
    for key, (title, number) in SECTION_MAP.items():
        if section_filter and key != section_filter:
            continue
        tools = raw.get(key, [])
        rendered = [
            {
                "tool": entry["tool"],
                "cmd":  entry["cmd"].replace("{target}", target),
                "desc": entry["desc"],
            }
            for entry in tools
        ]
        workflow.append({"number": number, "title": title, "tools": rendered})

    return workflow
