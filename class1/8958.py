t = int(input())
cases = []

for i in range(t):
    cases.append(input())

for case in cases:
    count = 0
    result = 0
    for char in case:
        if char == "O":
            count += 1
            result += count
        elif char == "X":
            count = 0
    print(result)