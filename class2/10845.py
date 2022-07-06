# 큐

import sys
from collections import deque

input = sys.stdin.readline
queue = deque()
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
        queue.append(value)
    elif command == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif command == 'size':
        print(len(queue))
    elif command == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif command == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif command == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[len(queue) - 1])