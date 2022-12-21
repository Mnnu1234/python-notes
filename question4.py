fruit=['banana','orange','mango','lemon',]
a=input("enter your fruit name:")

if a in fruit:
    print('the fruit is already exixt in the list ')
else:
    fruit.append(a)
    print(fruit)
