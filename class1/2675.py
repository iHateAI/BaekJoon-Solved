# 문자열 반복

t = int(input())
test_cnt = []
test_str = []
for _ in range(t):
    cnt, str = input().split(" ")
    test_cnt.append(int(cnt))
    test_str.append(str)

for i in range(t):
    for char in test_str[i]:
        print(char * test_cnt[i], end="")
    print()