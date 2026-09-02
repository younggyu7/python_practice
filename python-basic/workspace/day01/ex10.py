print("=" * 3)
print("#문제1")
i = 0
while i < 16:
    print(i)
    i += 1

print("=" * 3)
print("#문제2")
i = 0
while i <= 100:
    print(i)
    i += 10

print("=" * 3)
print("#문제3")
i = 1
while i <= 50:
    if i % 2 != 0:
        print(i)
    i += 2

print("=" * 3)
print("#문제4")
i = 1
sum = 0
while i <= 50:
    sum += i
    i += 1
print(sum)

print("=" * 3)
print("#문제5")
i = 0
sum = 0
while i <= 100:
    if i % 2 == 0:
        sum += i
    i += 2
print(sum)
