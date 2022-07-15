num = list(map(int, input().split()))
diff = num[1] - num[0]
result = None

if diff == 1:
    result = "ascending"
elif diff == -1:
    result = "descending"

for i in range(1, len(num) - 1):
    if num[i + 1] - num[i] != diff:
        result = "mixed"

print(result)