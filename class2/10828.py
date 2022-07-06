# 스택

import sys

input = sys.stdin.readline
n = int(input())

result = []

for _ in range(n):
    statement = input().split()
    if len(statement) > 1:
        command = statement[0]
        value = statement[1]
    else:
        command = statement[0]

    if command == 'push':
        result.append(value)
    elif command == 'pop':
        if len(result) == 0:
            print(-1)
        else:
            print(result.pop())
    elif command == 'size':
        print(len(result))
    elif command == 'empty':
        if len(result) == 0:
            print(1)
        else:
            print(0)
    elif command == 'top':
        if len(result) == 0:
            print(-1)
        else:
            idx = len(result)
            print(result[idx - 1])