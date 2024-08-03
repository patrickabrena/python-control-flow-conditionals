#two types of operators we'll talk about

#Math and Logical Operators

#Math operators as the ones that perform arithmetic on ints
#logical operators used to check if statement is true or false (and, or, not)

#basic example of using LOGICAL OPERATOR

a = True
b = True

if a and b == True:
    print("a and b are true")


#showing example with the confusing "not" operator
c = False
d = True

if not(c) or not(d):
    print("this is true")
#this prints true because not c == not false therefore c is true