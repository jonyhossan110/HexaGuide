import json
import os

_HERE = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(_HERE, "..", "data", "commands.json")

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


def load_commands() -> dict:
    path = os.path.abspath(DATA_FILE)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def build_workflow(target: str, section_filter: str | None = None) -> list[dict]:
    raw = load_commands()

    if section_filter and section_filter not in SECTION_MAP:
        raise ValueError(
            f"Unknown section '{section_filter}'. "
            f"Valid: {', '.join(SECTION_MAP.keys())}"
        )

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
