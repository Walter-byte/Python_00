w = input ("write a word for searching vowels... ")
v = ["a", "e", "i", "o", "u"]
found = {}
found["a"] = 0
found["e"] = 0
found["i"] = 0
found["o"] = 0
found["u"] = 0

for letter in w:
    if letter in v:
        found [letter] += 1
for k,v in found.items():
    print(k, "was found", v, "time(s).")
