n, k = map(int, input().split())
arr = []
count = 0
for _ in range(n):
    arr.append(int(input()))

arr.sort(reverse=True)

for money in arr:
    if money > k:
        continue
    if k != 0:
        count = count + (k // money)
        k = k % money
    else:
        break

print(count)