word = input()
capitals = [value for value in [word[i] if word[i].isupper() else 0 for i in range(len(word))] if value != 0]
print(word.upper() if len(capitals) > (len(word) - len(capitals)) else word.lower())
