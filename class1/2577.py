# 숫자의 개수

a = int(input())
b = int(input())
c = int(input())

li = [0] * 10

result_mul = a * b * c
result_str = str(result_mul)

for i in range(len(result_str)):
    for j in range(10):
        if str(j) == result_str[i]:
            li[j] += 1
            break

for i in range(10):
    print(li[i])