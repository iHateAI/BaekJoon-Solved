# 구구단

def gugu(n):
    for i in range(1, 10):
        print("{} * {} = {}".format(n, i, n * i))

n = int(input())
gugu(n)