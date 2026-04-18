"""Tests for report saving in hexaguide.main."""
import os
import glob
import pytest
from hexaguide.engine import build_workflow
from hexaguide.main import _save_report, _sanitize
from hexaguide import __version__


class TestSanitize:
    def test_strips_forward_slash(self):
        assert "/" not in _sanitize("192.168.1.1/admin")

    def test_strips_colon(self):
        assert ":" not in _sanitize("example.com:8080")

    def test_strips_backslash(self):
        assert "\\" not in _sanitize("path\\to\\thing")

    def test_strips_asterisk(self):
        assert "*" not in _sanitize("*.example.com")

    def test_plain_domain_unchanged(self):
        assert _sanitize("example.com") == "example.com"


class TestSaveReport:
    def test_report_file_created(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        wf = build_workflow("example.com")
        path = _save_report("example.com", wf)
        assert os.path.isfile(path)

    def test_report_in_reports_subdir(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        wf = build_workflow("example.com")
        path = _save_report("example.com", wf)
        assert path.startswith(os.path.join("reports", ""))

    def test_filename_starts_with_target(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        wf = build_workflow("mysite.com")
        path = _save_report("mysite.com", wf)
        assert os.path.basename(path).startswith("mysite.com_")

    def test_filename_ends_with_txt(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        wf = build_workflow("example.com")
        path = _save_report("example.com", wf)
        assert path.endswith(".txt")

    def test_filename_contains_timestamp(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        wf = build_workflow("example.com")
        path = _save_report("example.com", wf)
        basename = os.path.basename(path)
        # format: example.com_YYYYMMDD_HHMMSS.txt  → len > len("example.com_.txt")
        assert len(basename) > len("example.com_.txt")


class TestReportContent:
    def test_contains_target(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        wf = build_workflow("targetsite.com")
        path = _save_report("targetsite.com", wf)
        assert "targetsite.com" in open(path).read()

    def test_contains_version(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        wf = build_workflow("example.com")
        path = _save_report("example.com", wf)
        assert __version__ in open(path).read()

    def test_contains_all_section_headings(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        wf = build_workflow("example.com")
        path = _save_report("example.com", wf)
        content = open(path).read()
        for heading in [
            "RECONNAISSANCE", "SUBDOMAIN ENUMERATION", "SCANNING",
            "DIRECTORY BRUTEFORCE", "VULNERABILITY SCAN",
            "EXPLOITATION SUGGESTIONS", "AUTHENTICATION TESTING", "SSL ANALYSIS",
        ]:
            assert heading in content, f"Missing section: {heading}"

    def test_contains_legal_notice(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        wf = build_workflow("example.com")
        path = _save_report("example.com", wf)
        assert "LEGAL NOTICE" in open(path).read()

    def test_contains_hexacyberlab(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        wf = build_workflow("example.com")
        path = _save_report("example.com", wf)
        assert "HexaCyberLab" in open(path).read()

    def test_reports_dir_auto_created(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        assert not os.path.isdir("reports")
        wf = build_workflow("example.com")
        _save_report("example.com", wf)
        assert os.path.isdir("reports")
