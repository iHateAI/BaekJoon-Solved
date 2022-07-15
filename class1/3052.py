numbers = []
results = []
for i in range(10):
    num = int(input())
    numbers.append(num % 42)

for i in numbers:
    if i not in results:
        results.append(i)

print(len(results))
