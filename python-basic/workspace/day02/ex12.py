# 리스트 컴퓨리헨션
nums = [1, 2, 3, 4, 5]
squares = [n * n for n in nums]
print(squares)

sq = []
for n in nums:
    sq.append(n * n)
print(sq)

# 조건 포함
even_nums = [n for n in nums if n % 2 == 0]
print(even_nums)

# 문자열 처리
words = ["apple", "banana", "cherry"]
caped = [word.upper() for word in words]
print(words)
print(caped)

matrix = [[10, 20], [30, 40]]  # 다중 리스트
flattened = [num for row in matrix for num in row]
print(flattened)
