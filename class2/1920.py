# 수 찾기

N = int(input())
A = set(list(map(int, input().split())))
M = int(input())
arr = list(map(int, input().split()))

for i in range(M):
    if arr[i] in A:
        print(1)
    else:
        print(0)