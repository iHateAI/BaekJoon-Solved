n = int(input())
data = []

for _ in range(n):
    wt = list(map(int, input().split()))
    data.append(wt)

for i in range(n):
    rank = 1
    for j in range(n):
        if i == j:
            continue
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            rank += 1
    print(rank)