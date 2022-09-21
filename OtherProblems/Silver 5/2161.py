# 카드1
# 구현

n = int(input())
card = list(range(1, n + 1))
result = []
while True:
    if len(card) == 1:
        result.append(card[0])
        break
    result.append(card.pop(0))
    card.append(card.pop(0))

for num in result:
    print(num, end=" ")