
#example for loop
favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisu', 'Chocolate Cake']

for i in favorites:
    print("I like ", i)




#example while loop
favorites1 = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisu', 'Chocolate Cake']

index = 2

while index < len(favorites1):
    print("I love {}".format(favorites1[index]))
    index += 1
#I love Churros
#I love Tiramisu
#I love Chocolate Cake

#that is what the output would be.
#IMPORTANT!: incrementing the count is needed to prevent infinite loop
#IMPORTANT!: print("I love {}".format(favorites1[index])) is correct NOT print("I love {}".format(favorites1)) otherwise i get infinite loop