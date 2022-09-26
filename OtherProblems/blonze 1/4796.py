# 캠핑
# 그리디, 수학

i = 1
while True:
    l, p, v = map(int, input().split())
    if l == 0 and p == 0 and v == 0:
        break
    if v % p >= l:
        print(f'Case {i}: {v // p * l + l}')
    else:
        print(f'Case {i}: {v // p * l + v % p}')
    i += 1