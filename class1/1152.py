# 단어의 개수

data = input()
data = data.strip()
data = data.split(' ')

if data[0] == '':
    print(0)
else:
    print(len(data))