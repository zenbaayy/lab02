# CSE325-2026-L02-M4RB-T4
"""Same tests, unmodified, against BEFORE and AFTER."""
import pytest
import cold_grades
import grades_refactored

QUALITY_BASELINE = "behaviour-preservation"
MODULES = [cold_grades, grades_refactored]


def call(module, rows):
    module.run(rows, False, None, None, None, None)


@pytest.mark.parametrize("module", MODULES)
def test_normal_report(module, capsys):
    call(module, ["Ali,90,80", "Sara,60,50"])
    assert capsys.readouterr().out == "Ali: 85.0 (A)\nSara: 55.0 (C)\nPassed: 2/2\n"


@pytest.mark.parametrize("module", MODULES)
def test_boundary_70_is_B_and_69_is_C(module, capsys):
    call(module, ["X,70", "Y,69"])
    out = capsys.readouterr().out
    assert "X: 70.0 (B)" in out and "Y: 69.0 (C)" in out


@pytest.mark.parametrize("module", MODULES)
def test_failing_and_malformed_rows(module, capsys):
    call(module, ["Z,10,20", "badrow"])
    assert capsys.readouterr().out == "Z: 15.0 (F)\nPassed: 0/1\n"
