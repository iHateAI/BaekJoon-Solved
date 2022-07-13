n = int(input())

data = {}

for _ in range(n):
    age, name = input().split()
    data[name] = age

result = sorted(data.items(), key=lambda x: x[1])

for val in result:
    print(val[0], val[1])