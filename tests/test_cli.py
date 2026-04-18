"""Tests for hexaguide.cli — argument parsing."""
import sys
import pytest
from hexaguide.cli import get_args
from hexaguide.engine import VALID_SECTIONS


def _parse(*args):
    """Helper: set sys.argv and call get_args()."""
    sys.argv = ["HexaGuide", *args]
    return get_args()


class TestTargetArgument:
    def test_target_parsed_correctly(self):
        args = _parse("example.com")
        assert args.target == "example.com"

    def test_ip_target(self):
        args = _parse("192.168.1.1")
        assert args.target == "192.168.1.1"

    def test_no_target_exits(self):
        sys.argv = ["HexaGuide"]
        with pytest.raises(SystemExit) as exc:
            get_args()
        assert exc.value.code != 0


class TestDefaultValues:
    def test_no_save_default_false(self):
        args = _parse("example.com")
        assert args.no_save is False

    def test_section_default_none(self):
        args = _parse("example.com")
        assert args.section is None


class TestNoSaveFlag:
    def test_long_flag(self):
        args = _parse("example.com", "--no-save")
        assert args.no_save is True


class TestSectionFlag:
    def test_long_flag(self):
        args = _parse("example.com", "--section", "recon")
        assert args.section == "recon"

    def test_short_flag(self):
        args = _parse("example.com", "-s", "ssl")
        assert args.section == "ssl"

    def test_all_valid_sections_accepted(self):
        for sec in VALID_SECTIONS:
            args = _parse("example.com", "--section", sec)
            assert args.section == sec

    def test_invalid_section_exits(self):
        sys.argv = ["HexaGuide", "example.com", "--section", "notvalid"]
        with pytest.raises(SystemExit) as exc:
            get_args()
        assert exc.value.code != 0


class TestVersionFlag:
    def test_version_long_exits_zero(self):
        sys.argv = ["HexaGuide", "--version"]
        with pytest.raises(SystemExit) as exc:
            get_args()
        assert exc.value.code == 0

    def test_version_short_exits_zero(self):
        sys.argv = ["HexaGuide", "-v"]
        with pytest.raises(SystemExit) as exc:
            get_args()
        assert exc.value.code == 0
