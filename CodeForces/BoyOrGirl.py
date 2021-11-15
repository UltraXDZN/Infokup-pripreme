word = input()

lenght = len(word)
is_male = True
repeated = ""
for character in word:
    if word.count(character) > 1 and character not in repeated:
        is_male = False
        lenght -= word.count(character)-1
        repeated += character

if lenght % 2 == 0:
    is_male = False

if not is_male and lenght % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")