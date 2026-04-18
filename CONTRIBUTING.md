# Contributing to HexaGuide

Thank you for your interest in improving HexaGuide!

---

## Getting Started

```bash
git clone https://github.com/jonyhossan110/HexaGuide.git
cd HexaGuide

# Install with dev dependencies
pip install -e ".[dev]"

# Verify everything works
HexaGuide --version
pytest
```

---

## How to Contribute

### 1. Add or improve commands

All commands live in `hexaguide/data/commands.json`.

Each entry must follow this structure exactly:

```json
{
  "tool": "tool-name",
  "cmd":  "tool-name --flags {target}",
  "desc": "One-line description of what this does"
}
```

**Always use `{target}` as the placeholder** — it gets replaced with the user's domain/IP at runtime.

**Available sections:** `recon`, `subdomain`, `scan`, `directory`, `vuln`, `exploit`, `auth`, `ssl`

After adding, run:
```bash
pytest tests/test_engine.py -v
HexaGuide example.com --no-save
```

---

### 2. Bug reports

Open an issue: https://github.com/jonyhossan110/HexaGuide/issues

Include:
- Python version (`python --version`)
- OS and version
- Exact command you ran
- Full terminal output / error

---

### 3. Feature requests

Open an issue with `[Feature]` in the title.

---

## Code Style

- Follow PEP 8
- Keep functions small and focused
- No new external dependencies beyond `rich`
- All commands must use `{target}` placeholder

---

## Running Tests

```bash
# All tests
pytest

# Specific file
pytest tests/test_engine.py -v

# With coverage
pytest --cov=hexaguide
```

---

## Legal Notice

Only contribute commands/tools intended for **authorized** penetration testing.
Never add tools designed for illegal access, DDoS attacks, or unauthorized surveillance.

---

Made with ❤ by [HexaCyberLab](https://hexacyberlab.com)
