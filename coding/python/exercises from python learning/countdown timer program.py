# a stopwatch
import time # a cool extension to create timers and staff like that

my_time = int(input("enter the time in seconds: "))

for x in reversed(range(0, my_time)):
    seconds = x % 60
    minutes = int(x /60) % 60
    hours = int(x /3600)

    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)  #stops for 1 second 

print("times up!")
