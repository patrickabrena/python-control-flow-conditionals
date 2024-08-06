#this example will show the time complexity of a for loop which is O(n^2)

import time
start_time = time.time()

#outer loop
for i in range(5):
    #inner loop
    for j in range(5):
        print(0, end = "") #the end = "" makes it so that the zeros are printed all in one line rather than separate
    print()#empty print statment will print after every loop in the outside loop

#going to print how long it took to finish iterating
print(round((time.time() - start_time), 2)) # rounding to 2 decimal places. 
#play around with the range in the either of loops and see how long it took to finish iterating