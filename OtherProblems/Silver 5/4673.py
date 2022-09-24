# 셀프 넘버
# 구현

nums = list(range(1, 10001))

def makeFunc(num):
    sum = num
    num = str(num)
    for n in num:
        sum += int(n)
    return sum

for i in range(1, 10001):
    result = makeFunc(i)
    if result in nums:
        nums.remove(result)

for num in nums:
    print(num)