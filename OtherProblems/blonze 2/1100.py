# 하얀 칸
# 구현

board = []
count = 0
for i in range(8):
    input_data = input()
    for j in range(8):
        if (i + j) % 2 == 0 and input_data[j] == 'F':
            count += 1

print(count)

