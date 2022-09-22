# 거스름돈
# 그리디

change = 1000 - int(input())
money = [500, 100, 50, 10, 5, 1]
count = 0

for price in money:
    if change >= price:
        count += change // price
        change %= price

print(count)