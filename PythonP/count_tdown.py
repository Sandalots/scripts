import time 
# create a simple timer for a countdown

def countdown(minutes):
    while minutes > 0:
        print(minutes)
        time.sleep(60)
        minutes -= 1
    return True

