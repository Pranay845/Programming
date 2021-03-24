"""
Time Module is used for doing stuff with Time.
"""

import time

initial = time.time()  # the time that starts counting from a given time

k = 0
while k < 45:  # a while loop for printing the statement
    print("This is me")
    time.sleep(2)  # this waits program for 2 seconds
    k += 1
print("While loop ran in", time.time() - initial, "Seconds")  # this returns the time which is being subtracted by
# The before time

initial2 = time.time()
for i in range(45):  # a for loop to do same thing
    print("This is me")
print("For loop ran in", time.time() - initial2, "Seconds")  # this returns the time which is being subtracted by

# The before time
# innermost one is time counting next changing the time to local time and last one changes from tuple to time
localtime = time.asctime(time.localtime(time.time()))
print(localtime)
