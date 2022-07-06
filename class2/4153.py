# 직각삼각형

cases = [

]

while True:
    n = list(map(int, input().split()))
    if n[0] == 0 and n[1] == 0 and n[2] == 0:
        break
    else:
        n.sort()
        cases.append(n)

for case in cases:
    if case[2] ** 2 == case[0] ** 2 + case[1] ** 2:
        print("right")
    else:
        print("wrong")