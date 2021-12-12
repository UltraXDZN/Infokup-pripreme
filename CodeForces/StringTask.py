word = input().lower()
vowels = ["a", "o", "y", "e", "u", "i"]
word_n = ""
for ch in word:
    if ch not in vowels:
        word_n += f".{ch}"

print(word_n)