# 펠린드롬수 풀이

while True:
    isPalindrome = True
    data = input()
    if data == '0':
        break
    idx = len(data) // 2

    for i in range(idx):
        if data[i] != data[len(data) - 1 - i]:
            isPalindrome = False
            break
    if isPalindrome:
        print('yes')
    else:
        print('no')