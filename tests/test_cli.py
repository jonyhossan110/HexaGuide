"""Tests for hexaguide.cli — argument parsing."""
import sys
import pytest
from hexaguide.cli import get_args


def _parse(*args):
    sys.argv = ["HexaGuide", *args]
    return get_args()


def test_target_required():
    sys.argv = ["HexaGuide"]
    with pytest.raises(SystemExit):
        get_args()


def test_basic_target():
    args = _parse("example.com")
    assert args.target == "example.com"
    assert args.no_save is False
    assert args.section is None


def test_no_save_flag():
    args = _parse("example.com", "--no-save")
    assert args.no_save is True


def test_section_flag():
    args = _parse("example.com", "--section", "recon")
    assert args.section == "recon"


def test_short_section_flag():
    args = _parse("example.com", "-s", "ssl")
    assert args.section == "ssl"


def test_invalid_section_exits():
    sys.argv = ["HexaGuide", "example.com", "--section", "notasection"]
    with pytest.raises(SystemExit):
        get_args()


def test_version_flag_exits():
    sys.argv = ["HexaGuide", "--version"]
    with pytest.raises(SystemExit):
        get_args()
