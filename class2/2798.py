# 블랙잭

n, m = map(int, input().split())
list = list(map(int, input().split()))

ans = 0

for i in range(0, n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if((list[i] + list[j] + list[k]) <= m and (list[i] + list[j] + list[k]) > ans):
                ans = list[i] + list[j] + list[k]

print(ans)