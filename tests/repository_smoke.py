from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
source = ROOT / "Student Marks Analyzer.py"
assert source.exists(), "main analyzer file is missing"
assert source.stat().st_size > 0, "main analyzer file is empty"
compile(source.read_text(encoding="utf-8"), str(source), "exec")
print("Student Marks Analyzer smoke check passed")
