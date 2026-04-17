# Changelog

All notable changes to HexaGuide will be documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [1.0.0] — 2025-01-01

### Added
- Initial public release
- 8 pentest phases: Recon, Subdomain, Scan, Directory, Vuln, Exploit, Auth, SSL
- 32 real-world commands across 8 phases using industry tools
- Rich terminal UI with colored output, panels, and tables
- Auto-saving timestamped reports to `reports/` directory
- `--section` flag for single-phase runs
- `--no-save` flag to suppress report output
- `--version` flag
- Global CLI entry point `HexaGuide` via `pip install .`
- Full `pyproject.toml` build configuration
- MIT License

---

## Upcoming

- `--output json` flag for machine-readable report export
- `--list-tools` flag to show available tools per section
- Interactive mode with menu selection
- Color themes (dark / light)
- Bash completion support
