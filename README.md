<div align="center">

```
  _   _                   ____       _     _
 | | | | _____  ____ _   / ___|_   _(_) __| | ___
 | |_| |/ _ \ \/ / _` | | |  _| | | | |/ _` |/ _ \
 |  _  |  __/>  < (_| | | |_| | |_| | | (_| |  __/
 |_| |_|\___/_/\_\__,_|  \____|\__,_|_|\__,_|\___|
```

**Web Penetration Testing Workflow Generator**

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![CI](https://img.shields.io/github/actions/workflow/status/HexaCyberLab/HexaGuide/ci.yml?style=flat-square&label=CI)](https://github.com/HexaCyberLab/HexaGuide/actions)
[![Version](https://img.shields.io/badge/version-1.0.0-red?style=flat-square)](CHANGELOG.md)
[![HexaCyberLab](https://img.shields.io/badge/by-HexaCyberLab-cyan?style=flat-square)](https://hexacyberlab.com)

*One command. Eight phases. 32 copy-ready pentest commands.*

</div>

---

## What is HexaGuide?

**HexaGuide** is a professional CLI tool that instantly generates a complete, structured web penetration testing workflow for any target domain or IP address.

Run one command → get a full, phase-by-phase pentest roadmap with real tools and copy-ready commands — saved as a timestamped report.

Built by **[Md. Jony Hassain](https://linkedin.com/in/md-jony-hassain/)** — Web Penetration Tester at **[HexaCyberLab](https://hexacyberlab.com)**.

---

## Demo

```
$ HexaGuide example.com
```

```
  _   _                   ____       _     _
 | | | | _____  ____ _   / ___|_   _(_) __| | ___
 | |_| |/ _ \ \/ / _` | | |  _| | | | |/ _` |/ _ \
 |  _  |  __/>  < (_| | | |_| | |_| | | (_| |  __/
 |_| |_|\___/_/\_\__,_|  \____|\__,_|_|\__,_|\___|

╭─────────────────────── ⬡ HexaGuide Pentest Report ───────────────────────╮
│  Target   example.com                                                     │
│  Version  v1.0.0                                                          │
│  Author   Md. Jony Hassain — HexaCyberLab                                │
│  Website  hexacyberlab.com                                                │
╰───────────────────────────────────────────────────────────────────────────╯

⚠  WARNING: Use only on systems you have written permission to test.

──── [1]  Reconnaissance ──────────────────────────────────────────────────────

    ╭─────────────────────────────────────────────────────────────────────╮
    │ Tool    │ nmap                                                       │
    │ Command │ nmap -sV -sC -O -T4 example.com                           │
    │ Purpose │ Detect open ports, services, and OS fingerprint           │
    ╰─────────────────────────────────────────────────────────────────────╯

    ... (32 commands across 8 phases) ...

╭──────────────────────────── ✔  Scan Complete ────────────────────────────╮
│  Report   reports/example.com_20250117_143022.txt                        │
│  Tip      All commands are copy-ready. Adjust wordlist paths as needed.  │
╰──────────────────────────────────────────────────────────────────────────╯
```

---

## Features

| Feature | Details |
|--------|---------|
| **8 pentest phases** | Recon → Subdomain → Scan → Directory → Vuln → Exploit → Auth → SSL |
| **32 real commands** | nmap, amass, nuclei, gobuster, nikto, sqlmap, hydra, sslscan & more |
| **Copy-ready output** | Every command has `{target}` replaced — just paste and run |
| **Auto-saved reports** | Timestamped `.txt` report in `reports/` after every run |
| **Section filter** | Run just one phase with `--section recon` |
| **Rich terminal UI** | Colored panels, tables, warnings via the `rich` library |
| **Global CLI** | Runs as `HexaGuide` anywhere after `pip install .` |
| **Zero bloat** | One dependency (`rich`). Clean modular code. |

---

## Installation

### Requirements
- Python 3.10+
- pip

### From GitHub (recommended)

```bash
git clone https://github.com/jonyhossan110/HexaGuide.git
cd HexaGuide
pip install .
```

### Verify

```bash
HexaGuide --version
# HexaGuide 1.0.0 by HexaCyberLab
```

---

## Usage

```bash
# Full workflow — all 8 phases
HexaGuide example.com

# Use an IP address
HexaGuide 192.168.1.1

# Run only one phase
HexaGuide example.com --section recon
HexaGuide example.com --section ssl
HexaGuide example.com -s vuln

# Skip saving report to disk
HexaGuide example.com --no-save

# Show version
HexaGuide --version

# Show help
HexaGuide --help
```

### Available Sections

| Flag | Phase |
|------|-------|
| `recon` | Reconnaissance |
| `subdomain` | Subdomain Enumeration |
| `scan` | Scanning |
| `directory` | Directory Bruteforce |
| `vuln` | Vulnerability Scan |
| `exploit` | Exploitation Suggestions |
| `auth` | Authentication Testing |
| `ssl` | SSL Analysis |

---

## Tools Included

| Phase | Tools |
|-------|-------|
| Reconnaissance | nmap, whois, theHarvester, dig |
| Subdomain Enumeration | sublist3r, amass, ffuf, assetfinder |
| Scanning | nmap (full), masscan, nmap (vuln), netcat |
| Directory Bruteforce | gobuster, ffuf, dirsearch, feroxbuster |
| Vulnerability Scan | nikto, nuclei, wpscan, sqlmap |
| Exploitation | metasploit, searchsploit, xsser, commix |
| Authentication | hydra, medusa, burpsuite (curl), jwt_tool |
| SSL Analysis | sslscan, testssl.sh, sslyze, openssl |

---

## Reports

Reports are auto-saved to `reports/<target>_<timestamp>.txt`:

```
reports/
└── example.com_20250117_143022.txt
```

The `reports/` directory is listed in `.gitignore` — your scan results stay local.

---

## Project Structure

```
HexaGuide/
├── hexaguide/              # Main package
│   ├── __init__.py         # Version metadata
│   ├── main.py             # Entry point + report saver
│   ├── cli.py              # argparse (target, --section, --no-save, --version)
│   ├── engine.py           # Loads commands.json, builds workflow
│   ├── formatter.py        # Rich terminal UI
│   └── modules/            # Per-phase module stubs (extensible)
│       ├── recon.py
│       ├── subdomain.py
│       ├── scan.py
│       ├── exploit.py
│       ├── auth.py
│       └── ssl.py
├── data/
│   └── commands.json       # All 32 pentest commands (8 sections × 4 tools)
├── tests/                  # Pytest test suite
│   ├── test_engine.py
│   ├── test_cli.py
│   └── test_report.py
├── reports/                # Auto-created, gitignored
├── .github/
│   ├── workflows/
│   │   ├── ci.yml          # CI on push/PR (Ubuntu, Windows, macOS)
│   │   └── release.yml     # Build + GitHub Release on tag
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   └── PULL_REQUEST_TEMPLATE.md
├── pyproject.toml          # Build config + entry_points
├── setup.py                # Legacy compatibility shim
├── requirements.txt        # Runtime dependency (rich)
├── requirements-dev.txt    # Dev dependencies (pytest)
├── MANIFEST.in
├── LICENSE                 # MIT
├── CHANGELOG.md
├── CONTRIBUTING.md
└── SECURITY.md
```

---

## Development

```bash
git clone https://github.com/jonyhassan110/HexaGuide.git
cd HexaGuide
python -m venv venv
source venv/bin/activate     # Windows: venv\Scripts\activate
pip install -e .
pip install pytest

# Run tests
pytest tests/ -v

# Run the tool
HexaGuide example.com
```

### Adding a new tool

Open `data/commands.json` and add an entry to the relevant section:

```json
{
  "tool": "my-tool",
  "cmd":  "my-tool --scan {target}",
  "desc": "What this tool does"
}
```

Use `{target}` as the placeholder — it gets replaced with the real domain at runtime.

---

## Legal Disclaimer

> **HexaGuide is intended exclusively for authorized penetration testing.**
>
> Only use this tool against systems you own or have **explicit written permission** to test.
> Unauthorized access is a criminal offense in most jurisdictions.
> HexaCyberLab and the author bear **zero responsibility** for any misuse.

---

## Author

**Md. Jony Hassain**  
Web Penetration Tester | Ethical Hacker | Cybersecurity Specialist  
Founder — [HexaCyberLab](https://hexacyberlab.com)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-md--jony--hassain-blue?style=flat-square&logo=linkedin)](https://linkedin.com/in/md-jony-hassain/)
[![GitHub](https://img.shields.io/badge/GitHub-HexaCyberLab-black?style=flat-square&logo=github)](https://github.com/HexaCyberLab)
[![Upwork](https://img.shields.io/badge/Upwork-Hire%20Me-green?style=flat-square&logo=upwork)](https://upwork.com/freelancers/~01fb775c14cdfe8922)

---

## License

MIT © 2025 [Md. Jony Hassain — HexaCyberLab](LICENSE)
