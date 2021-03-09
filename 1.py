from datetime import datetime
import time
import random

##rdm = random.randrange(0, 6)

# if Var were before the loop, rdm time is just one selected. and if it is in the loop,
# it could be more.

odds =[1,3,5,7,9,11]

# time_now = datetime.today()
# right_this_time = time_now.minute

for i in range (8):
    right_this_minute=datetime.today().minute
    #for calculating time in each loop
    rnd = random.randrange(0, 20)
    if right_this_minute in odds:
        print("the minute is {} => odd minute".format(right_this_minute))
    else:
        print("the minute is {} =>not an odd".format(right_this_minute))
    print("<<<wait time is {}>>> ".format(rnd))    
    time.sleep(rnd)
