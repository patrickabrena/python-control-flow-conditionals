############################################################

#https://www.youtube.com/watch?v=yCZBnjF4_tU 

#Example from the video to mimic a vending machine using break statement in a while loop with available_candies set to 4
available_candies = 4

x = int(input("How many candies do you want?"))

#choose an increment variable, i in this case
i = 1
while i <= x:

    if i > available_candies:
        print("Out of Stock")
        break
#the break statements exits the while loop

    print("Candy")
    i += 1


#Print numbers between 1 and 30 but don't print numbers divisible by 3 pr 5 using the modulo operator %
#example below will be using a for loop
for i in range(1 , 30):
    if i%3==0 or i%5==0:
        continue
#the continue statement will not break the loop, but just skip the remaining statements that fufil the if statment
    print(i)
#printing "i" will include the numbers up to 30 excluding those divisible by 3 and 5



#Example below will use pass statment
#Scenario is you want to print the numbers between 1 and 30 but exclude odd numbers
for j in range(1, 20):

    if (j%2 != 0):
        pass
    else:
        print(j)
#the pass is used when needing to fill an otherwise empty if block. without it, the code here would throw and error