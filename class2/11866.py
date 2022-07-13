from collections import deque

n, k = map(int, input().split())

queue = deque([i for i in range(1, n + 1)])
result = []

for _ in range(n):
    for _ in range(k - 1):
        queue.append(queue.popleft())
    result.append(str(queue.popleft()))

print("<" + ", ".join(result) + ">")

