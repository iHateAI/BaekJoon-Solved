# 별 찍기 - 2

def star(n):
    for i in range(1, n + 1):
        for j in range(0, n - i):
            print(" ", end="")
        for k in range(i):
            print("*", end="")
        print()

n = int(input())
star(n)
