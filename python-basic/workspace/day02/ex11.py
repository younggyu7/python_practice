# list 반복
fruits = ["apple", "banana", "cherry"]

for fr in fruits:
    print(fr)

# 문자열 반복
word = "hello"
for char in word:
    print(char)


# range() : 지정한 범위만큼의 수를 만들어주는 함수
for i in range(1, 6):
    print(i)

arr = [1, 2, 3, 4]
for i in range(0, len(arr), 2):
    print(arr[i])

t = (1, 2, 3, 4)
for i in range(0, len(t), 2):
    print(t[i])

str = "hello"
for i in str[::2]:
    print(i)

arr1 = [1, 2, 3, 4]
for i in arr1[::2]:
    print(i)

# dict반복
info = {"name": "pikachu", "age": 10, "height": 234.5}

for k in info.keys():
    print(k)

for v in info.values():
    print(v)

for k, v in info.items():
    print(k, "/ ", v)
print("=" * 30)

# 키, 값, 인덱스번호도 필요할 때
# enumerate() -> index, (k, v)
# print(enumerate(info.items()))
for i, (k, v) in enumerate(info.items(), start=1):
    print(i, k, v)

# ----------------------------------
lst = 1, 2, 3  # packing
a, b, c = (
    lst  # unpacking : lst 원소 갯수에 안 맞추면 오류, lst가 튜플이 아니라 리스트 여도 무관
)
print(a)
print(b)
print(c)
print("-" * 30)
for i, k in enumerate(arr):
    print(i, ": ", k)
