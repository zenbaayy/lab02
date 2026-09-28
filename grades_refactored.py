# CSE325-2026-L02-M4RB-T3
"""AFTER version: only the ACCEPTED changes applied (same public entry point)."""

QUALITY_BASELINE = "after"

GRADE_BOUNDARIES = ((85, "A"), (70, "B"), (55, "C"))


def letter_grade(average: float) -> str:
    for minimum, letter in GRADE_BOUNDARIES:
        if average >= minimum:
            return letter
    return "F"


def load_records(rows: list[str]) -> dict[str, list[int]]:
    student_records = {}
    for row in rows:
        parts = row.split(",")
        if len(parts) < 2:
            continue
        student_records[parts[0].strip()] = [int(x) for x in parts[1:]]
    return student_records


def calculate_average(marks: list[int]) -> float:
    return sum(marks) / len(marks)


def print_report(student_records: dict[str, list[int]]) -> None:
    passed = 0
    for name, marks in student_records.items():
        average = calculate_average(marks)
        grade = letter_grade(average)
        print(f"{name}: {average:.1f} ({grade})")
        if grade != "F":
            passed += 1
    print(f"Passed: {passed}/{len(student_records)}")


# Signature kept identical so existing callers do not break (rejected suggestion:
# removing the unused parameters would change the public API).
def run(rows, verbose=None, flag=None, mode=None, extra=None, path=None):
    print_report(load_records(rows))
