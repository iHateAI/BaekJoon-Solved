# 분해합

N = int(input())

result = 0

for i in range(1, N):
    temp_sum = i
    for j in str(i):
        temp_sum += int(j)
    if temp_sum == N:
        result = i
        break
    else:
        result = 0

print(result)