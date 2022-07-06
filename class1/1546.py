# 평균

N = int(input())
score = list(map(int, input().split(" ")))
M = max(score)
sum = 0
for i in range(len(score)):
    score[i] = score[i] / M * 100
    sum += score[i]

avg = sum / len(score)
print(round(avg, 2))
