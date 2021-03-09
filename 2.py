w = input ("write a word for me... ")
v = ["a", "e", "i", "o", "u"]
found = []
for letter in w:
    if letter in v:
        if letter not in found:
            found.append(letter)
for vowel in found:
    print(vowel)
