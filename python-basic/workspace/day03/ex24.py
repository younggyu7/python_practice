# import os

# print(os.getcwd())

from pathlib import Path

print(Path(__file__).resolve())
print(Path(__file__).resolve().parent)
print(Path(__file__).resolve().parent.parent)

ROOT = Path(__file__).resolve().parent.parent

with open(ROOT / "a.txt", "r", encoding="utf-8") as f:
    data = f.read()
    print(data)
