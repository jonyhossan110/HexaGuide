<div align="center">

```
  _   _                   ____       _     _
 | | | | _____  ____ _   / ___|_   _(_) __| | ___
 | |_| |/ _ \ \/ / _` | | |  _| | | | |/ _` |/ _ \
 |  _  |  __/>  < (_| | | |_| | |_| | | (_| |  __/
 |_| |_|\___/_/\_\__,_|  \____|\__,_|_|\__,_|\___|
```

**Web Penetration Testing Workflow Generator**

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![CI](https://img.shields.io/github/actions/workflow/status/jonyhossan110/HexaGuide/ci.yml?style=flat-square&label=CI&logo=github)](https://github.com/jonyhossan110/HexaGuide/actions)
[![Version](https://img.shields.io/badge/version-1.0.0-red?style=flat-square)](CHANGELOG.md)
[![HexaCyberLab](https://img.shields.io/badge/by-HexaCyberLab-cyan?style=flat-square)](https://hexacyberlab.com)

*One command. Eight phases. 32 copy-ready pentest commands.*

</div>

---

## What is HexaGuide?

**HexaGuide** is a professional CLI tool that instantly generates a complete, structured web penetration testing workflow for any target domain or IP address.

Run one command → get a full, phase-by-phase pentest roadmap with real tools and copy-ready commands — automatically saved as a timestamped report.

Built by **[Md. Jony Hassain](https://linkedin.com/in/md-jony-hassain/)** — Web Penetration Tester at **[HexaCyberLab](https://hexacyberlab.com)**.

---

## Quick Demo

```
$ HexaGuide example.com
```

```
  _   _                   ____       _     _
 | | | | _____  ____ _   / ___|_   _(_) __| | ___
 | |_| |/ _ \ \/ / _` | | |  _| | | | |/ _` |/ _ \
 |  _  |  __/>  < (_| | | |_| | |_| | | (_| |  __/
 |_| |_|\___/_/\_\__,_|  \____|\__,_|_|\__,_|\___|

╭────────── ⬡ HexaGuide — Pentest Workflow ──────────╮
│   Target   example.com                             │
│   Version  v1.0.0                                  │
│   Author   Md. Jony Hassain — HexaCyberLab         │
│   Web      hexacyberlab.com                        │
│   GitHub   github.com/jonyhossan110/HexaGuide      │
╰────────────────────────────────────────────────────╯

⚠  WARNING: Use only on systems you have written permission to test.

──── [1]  Reconnaissance ──────────────────────────────────

    ╭─────────────────────────────────────────────────────╮
    │ Tool    │ nmap                                      │
    │ Command │ nmap -sV -sC -O -T4 example.com           │
    │ Purpose │ Detect open ports, services, OS fingerprint│
    ╰─────────────────────────────────────────────────────╯
    ... (32 commands across 8 phases)

╭──────────────── ✔  Scan Complete ───────────────────╮
│  Report  reports/example.com_20250101_120000.txt    │
╰─────────────────────────────────────────────────────╯
```

---

## Features

| Feature | Details |
|---------|---------|
| **8 pentest phases** | Recon → Subdomain → Scan → Directory → Vuln → Exploit → Auth → SSL |
| **32 real commands** | nmap, amass, nuclei, gobuster, nikto, sqlmap, hydra, sslscan & more |
| **Copy-ready output** | `{target}` replaced with your domain — paste and run immediately |
| **Auto-saved reports** | Timestamped `.txt` report saved to `reports/` after every scan |
| **Single-phase mode** | `--section recon` runs just one phase |
| **Rich terminal UI** | Colored panels, tables, legal warning banner |
| **Global CLI** | Run as `HexaGuide` anywhere after `pip install .` |
| **Zero bloat** | Only one runtime dependency: `rich` |

---

## Installation

### Requirements

- Python **3.10** or newer
- pip

### Step 1 — Clone the repository

```bash
git clone https://github.com/jonyhossan110/HexaGuide.git
cd HexaGuide
```

### Step 2 — Install (choose one)

**Option A — Standard install (recommended)**
```bash
pip install .
```

**Option B — Editable install (for development)**
```bash
pip install -e .
```

**Option C — Install with dev/test tools**
```bash
pip install -e ".[dev]"
```

### Step 3 — Verify

```bash
HexaGuide --version
# HexaGuide 1.0.0 — by HexaCyberLab
```

---

## Usage

```bash
# Full workflow — all 8 phases
HexaGuide example.com

# Use an IP address
HexaGuide 192.168.1.100

# Run only one phase
HexaGuide example.com --section recon
HexaGuide example.com --section ssl
HexaGuide example.com -s vuln

# Skip saving the report to disk
HexaGuide example.com --no-save

# Show version
HexaGuide --version

# Show help
HexaGuide --help
```

### All Options

| Flag | Short | Description |
|------|-------|-------------|
| `--section SECTION` | `-s` | Run only one phase |
| `--no-save` | | Skip writing report to disk |
| `--version` | `-v` | Show version and exit |
| `--help` | `-h` | Show help and exit |

### Available Sections

| Value | Phase |
|-------|-------|
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
| Scanning | nmap (full), masscan, nmap (vuln scripts), netcat |
| Directory Bruteforce | gobuster, ffuf, dirsearch, feroxbuster |
| Vulnerability Scan | nikto, nuclei, wpscan, sqlmap |
| Exploitation | metasploit, searchsploit, xsser, commix |
| Authentication | hydra, medusa, burpsuite (curl), jwt_tool |
| SSL Analysis | sslscan, testssl.sh, sslyze, openssl |

---

## Reports

Reports are automatically saved after every scan:

```
reports/
└── example.com_20250101_143022.txt
```

Each report includes:
- Target and timestamp
- All 8 phases with tool names, commands, and descriptions
- Legal notice

The `reports/` directory is listed in `.gitignore` — your results stay local.

---

## Development

### Setup

```bash
git clone https://github.com/jonyhossan110/HexaGuide.git
cd HexaGuide

# Install with dev dependencies (includes pytest)
pip install -e ".[dev]"
```

### Run Tests

```bash
# Run full test suite
pytest

# Run with verbose output
pytest -v

# Run only one test file
pytest tests/test_engine.py -v
```

### Add a New Tool

Open `hexaguide/data/commands.json` and add an entry to any section:

```json
{
  "tool": "my-tool",
  "cmd":  "my-tool --flag {target}",
  "desc": "What this tool does in one line"
}
```

Always use `{target}` — it gets replaced with the real domain at runtime.

---

## Project Structure

```
HexaGuide/
├── hexaguide/                  # Main Python package
│   ├── __init__.py             # Version and metadata
│   ├── main.py                 # Entry point + report saver
│   ├── cli.py                  # argparse (--section, --no-save, --version)
│   ├── engine.py               # Loads commands.json, builds workflow
│   ├── formatter.py            # Rich terminal UI
│   ├── data/
│   │   └── commands.json       # 32 pentest commands across 8 sections
│   └── modules/                # Extensible per-phase stubs
│       ├── recon.py
│       ├── subdomain.py
│       ├── scan.py
│       ├── exploit.py
│       ├── auth.py
│       └── ssl.py
├── tests/                      # pytest test suite (3 files, 30+ tests)
│   ├── test_engine.py
│   ├── test_cli.py
│   └── test_report.py
├── reports/                    # Auto-created, gitignored
├── .github/
│   ├── workflows/
│   │   ├── ci.yml              # CI: Ubuntu + Windows + macOS × Python 3.10–3.12
│   │   └── release.yml         # Auto GitHub Release on git tag
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   └── PULL_REQUEST_TEMPLATE.md
├── conftest.py                 # pytest root config
├── pyproject.toml              # Build config, entry_points, dev extras
├── setup.py                    # Legacy pip compatibility shim
├── requirements.txt            # Runtime: rich
├── requirements-dev.txt        # Dev: pytest, pytest-cov
├── MANIFEST.in                 # Source distribution file includes
├── LICENSE                     # MIT
├── CHANGELOG.md
├── CONTRIBUTING.md
└── SECURITY.md
```

---

## Troubleshooting

**`HexaGuide: command not found`**
```bash
# Make sure pip scripts folder is in your PATH
# On Linux/macOS:
export PATH="$HOME/.local/bin:$PATH"
# On Windows, run in the venv or use:
python -m hexaguide.main example.com
```

**`FileNotFoundError: commands.json`**
```bash
# Reinstall cleanly
pip install --force-reinstall .
```

**CI failing with `pytest: not found`**
```bash
# Install with dev extras
pip install -e ".[dev]"
```

---

## Legal Disclaimer

> **HexaGuide is designed exclusively for authorized penetration testing.**
>
> Only use this tool against systems you **own** or have **explicit written permission** to test.
> Unauthorized access is a criminal offense in most jurisdictions worldwide.
> HexaCyberLab and the author bear **zero responsibility** for any misuse of this tool.

---

## Author

**Md. Jony Hassain**
Web Penetration Tester | Ethical Hacker | Cybersecurity Specialist
Founder — [HexaCyberLab](https://hexacyberlab.com)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-md--jony--hassain-blue?style=flat-square&logo=linkedin)](https://linkedin.com/in/md-jony-hassain/)
[![GitHub](https://img.shields.io/badge/GitHub-jonyhossan110-black?style=flat-square&logo=github)](https://github.com/jonyhossan110)
[![Upwork](https://img.shields.io/badge/Upwork-Hire%20Me-green?style=flat-square&logo=upwork)](https://upwork.com/freelancers/~01fb775c14cdfe8922)
[![Instagram](https://img.shields.io/badge/Instagram-hexacyberlab-E4405F?style=flat-square&logo=instagram)](https://instagram.com/hexacyberlab/)

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to add tools, report bugs, and submit pull requests.

---

## License

MIT © 2025 [Md. Jony Hassain — HexaCyberLab](LICENSE)
