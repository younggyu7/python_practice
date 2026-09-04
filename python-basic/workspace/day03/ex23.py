# 전체 읽기
with open("a.txt", "r", encoding="utf-8") as f:
    data = f.read()
    print(data)

print("-" * 40)

# 한줄씩 읽기
with open("a.txt", "r", encoding="utf-8") as f:
    line1 = f.readline()
    line2 = f.readline()
    print(line1)
    print(line2)

print("-" * 40)

# 모든 줄 리스트로 읽기
with open("a.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    print(lines)

with open("a.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())

import os

print(os.getcwd())
