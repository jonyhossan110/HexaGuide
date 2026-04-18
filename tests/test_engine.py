"""Tests for hexaguide.engine — workflow builder."""
import pytest
from hexaguide.engine import build_workflow, load_commands, SECTION_MAP


def test_load_commands_returns_dict():
    data = load_commands()
    assert isinstance(data, dict)
    assert len(data) == 8


def test_all_sections_present():
    data = load_commands()
    for key in SECTION_MAP:
        assert key in data, f"Missing section: {key}"


def test_each_section_has_minimum_tools():
    data = load_commands()
    for key in SECTION_MAP:
        assert len(data[key]) >= 3, f"Section '{key}' has fewer than 3 tools"


def test_build_workflow_returns_all_sections():
    wf = build_workflow("example.com")
    assert len(wf) == 8


def test_target_replaced_in_commands():
    wf = build_workflow("testdomain.com")
    for section in wf:
        for entry in section["tools"]:
            assert "testdomain.com" in entry["cmd"]
            assert "{target}" not in entry["cmd"]


def test_section_filter_returns_one_section():
    wf = build_workflow("example.com", section_filter="recon")
    assert len(wf) == 1
    assert wf[0]["title"] == "Reconnaissance"


def test_invalid_section_raises_value_error():
    with pytest.raises(ValueError):
        build_workflow("example.com", section_filter="invalid_section")


def test_workflow_structure_keys():
    wf = build_workflow("example.com")
    for section in wf:
        assert "number" in section
        assert "title" in section
        assert "tools" in section
        for tool in section["tools"]:
            assert "tool" in tool
            assert "cmd" in tool
            assert "desc" in tool


def test_all_section_filters():
    for key in SECTION_MAP:
        wf = build_workflow("example.com", section_filter=key)
        assert len(wf) == 1
