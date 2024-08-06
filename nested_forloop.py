#going to look at nested for floop in pypthon


#example below is if you need to iterate over two lists

list1 = [1,2,3,4,5,6,7,8,9]
list2 = [1,2,3,4,5,6,7,8,9]

#start with a count variable declared at 0. this will go up for as long as the for loop is running\

count = 0
#outer loop
for x in list1: #outer loop will run 9 times
    count += 1 #increment the count variable
    #inner loop
    for y in list2: #9 x 9 = 81
        count += 1
        print(count) #printing count here while in the nested for loop will print the incremented count

print("The final count is {}".format(count)) #printing the count outisde of the for looop will just print the total count