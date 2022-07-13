from collections import deque
import sys
queue = deque()

def input():
    return sys.stdin.readline().rstrip()

n = int(input())

for _ in range(n):
    statement = input().split()
    if len(statement) == 2:
        command = statement[0]
        value = statement[1]
    else:
        command = statement[0]

    if command == 'push_front':
        queue.appendleft(value)
    elif command == 'push_back':
        queue.append(value)
    elif command == 'pop_front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif command == 'pop_back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop())
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
            print(queue[-1])