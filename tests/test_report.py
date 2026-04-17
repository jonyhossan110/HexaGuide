"""Tests for report saving in hexaguide.main."""
import os
import glob
import sys
import pytest
from hexaguide.engine import build_workflow
from hexaguide.main import _save_report, _sanitize


def test_sanitize_target():
    assert "/" not in _sanitize("192.168.1.1/admin")
    assert ":" not in _sanitize("example.com:8080")


def test_report_saved_to_disk(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    wf = build_workflow("example.com")
    path = _save_report("example.com", wf)
    assert os.path.isfile(path)


def test_report_contains_target(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    wf = build_workflow("target-site.com")
    path = _save_report("target-site.com", wf)
    content = open(path).read()
    assert "target-site.com" in content


def test_report_contains_all_sections(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    wf = build_workflow("example.com")
    path = _save_report("example.com", wf)
    content = open(path).read()
    for heading in ["RECONNAISSANCE", "SCANNING", "SSL ANALYSIS"]:
        assert heading in content


def test_report_filename_has_timestamp(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    wf = build_workflow("example.com")
    path = _save_report("example.com", wf)
    basename = os.path.basename(path)
    # format: example.com_YYYYMMDD_HHMMSS.txt
    assert basename.startswith("example.com_")
    assert basename.endswith(".txt")
    assert len(basename) > len("example.com_.txt")
