n = int(input())
numbers = []

for i in range(n):
    a, b = map(int, input().split())
    numbers.append(a + b)

for i in range(n):
    print(numbers[i])