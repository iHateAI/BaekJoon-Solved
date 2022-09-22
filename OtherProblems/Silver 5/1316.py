# 그룹 단어 체커
# 구현

n = int(input())
count = 0
for _ in range(n):
    word = input()
    li = []
    isGroupWord = True
    li.append(word[0])
    for i in range(len(word) - 1):
        if word[i] != word[i + 1]:
            if word[i + 1] in li:
                isGroupWord = False
                break
            else:
                li.append(word[i + 1])
    if isGroupWord:
        count += 1

print(count)