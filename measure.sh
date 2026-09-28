#!/usr/bin/env bash
# Exact commands for Task 1 (baseline) and Task 3 (after). Paste output VERBATIM.
pip install ruff radon
for f in cold_grades.py grades_refactored.py; do
  echo "=== $f ==="
  ruff check --select E,F,B,S,UP,RUF $f
  radon cc -s -a $f          # cyclomatic complexity
  radon raw $f               # line counts
done
pytest -q                     # behaviour preserved?
git diff --stat <baseline_hash> <after_hash>
