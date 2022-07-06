# 이항 계수 1

def factorial(n):
    if n <= 1:
        return 1
    if n > 1:
        return n * factorial(n - 1)

n, k = map(int, input().split())

result = factorial(n) // (factorial(k) * factorial(n - k))
print(result)