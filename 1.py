from datetime import datetime
import time
import random

##rdm = random.randrange(0, 6)

# if Var were before the loop, rdm time is just one selected. and if it is in the loop,
# it could be more.

odds =[1,3,5,7,9,11]

right_this_minute=datetime.today().minute
# time_now = datetime.today()
# right_this_time = time_now.minute

for i in range (8):
    rnd = random.randrange(0,5)
    if right_this_minute in odds:
        print("odd minute")
    else:
        print("not an odd")
    print(rnd)    
    time.sleep(rnd)