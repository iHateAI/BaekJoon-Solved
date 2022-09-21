# 전자레인지
# 그리디

t = int(input())

a = 300
b = 60
c = 10

count_a = 0
count_b = 0
count_c = 0

if t % c != 0:
    print(-1)
else:
    if t >= a:
        count_a += t // a
        t = t % a
    if t >= b:
        count_b += t // b
        t = t % b
    if t >= c:
        count_c += t // c
        t = t % c

    print(f"{count_a} {count_b} {count_c}")

