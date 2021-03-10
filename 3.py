phrase = "!Salam Va vaght bekheyr !"
ph_list = list(phrase)
#ebarat to list
print(phrase)
print(ph_list)
for i in range (2):
    ph_list.pop()
ph_list.pop(0)
ph_list.remove("V")
ph_list.remove(" ")
ph_list.insert(2, ph_list.pop(15))
ph_list.insert(3, ph_list.pop(16))
ph_list.insert(4, ph_list.pop(13))
ph_list.remove("l")
ph_list.insert(6, ph_list.pop())
for i in range (12):
    ph_list.pop()
new_phrase = "".join(ph_list)
#list to ebarat
print(ph_list)
print(new_phrase)
