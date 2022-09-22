# 세탁소 사장 동혁
# 그리디

t = int(input())
QUARTER = 25
DIME = 10
NICKEL = 5
PENNY = 1

for _ in range(t):
    q_count = 0
    d_count = 0
    n_count = 0
    p_count = 0

    case = int(input())

    if QUARTER <= case:
        q_count = case // QUARTER
        case %= QUARTER

    if DIME <= case:
        d_count = case // DIME
        case %= DIME

    if NICKEL <= case:
        n_count = case // NICKEL
        case %= NICKEL

    if PENNY <= case:
        p_count = case // PENNY

    print(f"{q_count} {d_count} {n_count} {p_count}")

