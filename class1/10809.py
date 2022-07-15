string = input()
alphabet = "abcdefghijklmnopqrstuvwxyz"

for char in alphabet:
    if char in string:
        print(string.index(char), end=" ")
    else:
        print(-1, end=" ")