N, X = map(int, input().split(" "))

li = [int(x) for x in input().split()]

for i in range(N):
    if li[i] < X:
        print(li[i], end=" ")