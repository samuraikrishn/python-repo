#countdown timer
import time
def timer(seconds):
    while seconds>0:
        print(f"Time left:: {seconds} seconds")
        time.sleep(1)
        seconds-=1
    print("Time's Up")
try:
    seconds=int(input("Enter the number for timer:"))
    timer(seconds)
except ValueError:
    print("Please enter valid integer")
