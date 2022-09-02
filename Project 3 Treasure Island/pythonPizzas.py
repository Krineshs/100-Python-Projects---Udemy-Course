print("Welcome to Python Pizza Deliveries!")

print("Small $15")
print("Medium $20")
print("Large $25")

pizzaSize = input("Please enter the size of pizza you want")
addPep = input("Do you want Peparoni?")
addCheese = input("Do you want Cheese?")
total = int(0)

if pizzaSize == "Small":
    total = 15
elif pizzaSize == "Medium":
    total = 20

elif pizzaSize == "Large":
    total = 25

else:
    print("Please enter a proper entry")

if addCheese == "Y":
    total + 1
else:
    print("")

if addPep == "Y":
    if pizzaSize == "Small":
        total + 2
    else:
        total + 3
else:
    print("")



print(total)


