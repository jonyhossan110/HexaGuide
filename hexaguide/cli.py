import argparse
from hexaguide import __version__

VALID_SECTIONS = [
    "recon", "subdomain", "scan", "directory",
    "vuln", "exploit", "auth", "ssl"
]


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="HexaGuide",
        description=(
            "HexaGuide — Web Penetration Testing Workflow Generator\n"
            "Built by HexaCyberLab | hexacyberlab.com"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  HexaGuide example.com\n"
            "  HexaGuide 192.168.1.1\n"
            "  HexaGuide example.com --section recon\n"
            "  HexaGuide example.com --no-save\n"
            "\nAvailable sections:\n"
            "  recon, subdomain, scan, directory, vuln, exploit, auth, ssl"
        ),
    )

    parser.add_argument(
        "target",
        help="Target domain or IP (e.g. example.com or 192.168.1.1)",
    )
    parser.add_argument(
        "--section", "-s",
        choices=VALID_SECTIONS,
        default=None,
        metavar="SECTION",
        help="Run only one section (recon/subdomain/scan/directory/vuln/exploit/auth/ssl)",
    )
    parser.add_argument(
        "--no-save",
        action="store_true",
        default=False,
        help="Skip saving the report to disk",
    )
    parser.add_argument(
        "--version", "-v",
        action="version",
        version=f"HexaGuide {__version__} by HexaCyberLab",
    )

    return parser.parse_args()
