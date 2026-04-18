"""Tests for hexaguide.engine — workflow builder and command loader."""
import pytest
from hexaguide.engine import (
    build_workflow,
    load_commands,
    SECTION_MAP,
    VALID_SECTIONS,
    DATA_FILE,
)
import os


class TestLoadCommands:
    def test_data_file_exists(self):
        assert os.path.isfile(DATA_FILE), f"commands.json not found at: {DATA_FILE}"

    def test_returns_dict(self):
        data = load_commands()
        assert isinstance(data, dict)

    def test_has_eight_sections(self):
        data = load_commands()
        assert len(data) == 8

    def test_all_section_keys_present(self):
        data = load_commands()
        for key in SECTION_MAP:
            assert key in data, f"Missing section in commands.json: '{key}'"

    def test_each_section_minimum_three_tools(self):
        data = load_commands()
        for key in SECTION_MAP:
            assert len(data[key]) >= 3, (
                f"Section '{key}' has {len(data[key])} tools — minimum 3 required"
            )

    def test_each_tool_has_required_keys(self):
        data = load_commands()
        for section_key, tools in data.items():
            for i, tool in enumerate(tools):
                for field in ("tool", "cmd", "desc"):
                    assert field in tool, (
                        f"Section '{section_key}', tool #{i} missing field '{field}'"
                    )

    def test_all_cmds_have_target_placeholder(self):
        data = load_commands()
        for section_key, tools in data.items():
            for tool in tools:
                assert "{target}" in tool["cmd"], (
                    f"Section '{section_key}', tool '{tool['tool']}' "
                    f"cmd missing {{target}} placeholder"
                )


class TestBuildWorkflow:
    def test_returns_all_eight_sections(self):
        wf = build_workflow("example.com")
        assert len(wf) == 8

    def test_section_structure_keys(self):
        wf = build_workflow("example.com")
        for section in wf:
            assert "number" in section
            assert "title" in section
            assert "tools" in section

    def test_tool_structure_keys(self):
        wf = build_workflow("example.com")
        for section in wf:
            for tool in section["tools"]:
                assert "tool" in tool
                assert "cmd" in tool
                assert "desc" in tool

    def test_target_replaced_in_all_commands(self):
        wf = build_workflow("mytarget.com")
        for section in wf:
            for tool in section["tools"]:
                assert "mytarget.com" in tool["cmd"], (
                    f"Target not found in: {tool['cmd']}"
                )
                assert "{target}" not in tool["cmd"], (
                    f"Placeholder still present in: {tool['cmd']}"
                )

    def test_ip_address_target(self):
        wf = build_workflow("192.168.1.100")
        for section in wf:
            for tool in section["tools"]:
                assert "192.168.1.100" in tool["cmd"]

    def test_section_filter_returns_one_section(self):
        wf = build_workflow("example.com", section_filter="recon")
        assert len(wf) == 1
        assert wf[0]["title"] == "Reconnaissance"
        assert wf[0]["number"] == "1"

    def test_all_section_filters_work(self):
        for key in VALID_SECTIONS:
            wf = build_workflow("example.com", section_filter=key)
            assert len(wf) == 1, f"Section filter '{key}' returned {len(wf)} sections"

    def test_invalid_section_raises_value_error(self):
        with pytest.raises(ValueError, match="Unknown section"):
            build_workflow("example.com", section_filter="invalid_phase")

    def test_none_filter_returns_all(self):
        wf = build_workflow("example.com", section_filter=None)
        assert len(wf) == 8

    def test_section_numbers_are_sequential(self):
        wf = build_workflow("example.com")
        numbers = [int(s["number"]) for s in wf]
        assert numbers == list(range(1, 9))
