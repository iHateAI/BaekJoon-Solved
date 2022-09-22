# 거스름돈
# 그리디

change = 1000 - int(input())

count = 0

if change >= 500:
    count += change // 500
    change %= 500

if change >= 100:
    count += change // 100
    change %= 100

if change >= 50:
    count += change // 50
    change %= 50

if change >= 10:
    count += change // 10
    change %= 10

if change >= 5:
    count += change // 5
    change %= 5

if change >= 1:
    count += change

print(count)