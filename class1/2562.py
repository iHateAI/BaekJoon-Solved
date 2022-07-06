# 최댓값

numbers = []

for i in range(9):
    numbers.append(int(input()))

max = max(numbers)

for i in range(9):
    if(numbers[i] == max):
        index = i + 1

print(max)
print(index)