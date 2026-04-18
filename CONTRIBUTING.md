# Contributing to HexaGuide

Thank you for your interest in improving HexaGuide!

---

## Getting Started

```bash
git clone https://github.com/HexaCyberLab/HexaGuide.git
cd HexaGuide
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -e .
```

---

## How to Contribute

### 1. Add or improve commands

All commands live in `data/commands.json`.

Each entry follows this structure:

```json
{
  "tool": "tool-name",
  "cmd":  "tool-name --flag {target}",
  "desc": "Short one-line description"
}
```

Use `{target}` as the placeholder — it gets replaced with the user's domain/IP at runtime.

**Sections available:** `recon`, `subdomain`, `scan`, `directory`, `vuln`, `exploit`, `auth`, `ssl`

---

### 2. Bug reports

Open an issue at:  
https://github.com/HexaCyberLab/HexaGuide/issues

Include:
- Python version
- OS
- Exact command run
- Full error output

---

### 3. Feature requests

Open an issue with the `[Feature]` prefix in the title.

---

## Code Style

- Follow PEP 8
- Keep functions small and single-purpose
- No external dependencies beyond `rich`

---

## Legal Notice

Only contribute commands/tools that are legal to use in authorized engagements.  
Never add tools designed for illegal access, DDoS, or data theft.

---

Made with ❤ by [HexaCyberLab](https://hexacyberlab.com)
