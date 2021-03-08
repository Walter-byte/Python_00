from datetime import datetime
odds =[1,3,5,7,9,11]
right_this_minute=datetime.today().minute

if right_this_minute in odds:
    print("odd minute")
else:
    print("not an odd")
