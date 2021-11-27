n = int(input())
word = input().lower()
alphabet = "abcdefghijklmnopqrstuvwxyz"

count = 0
for letter in alphabet:
    if letter in word:
        count += 1
        word = word.replace(letter, '')
print(["NO", "YES"][count == 26])