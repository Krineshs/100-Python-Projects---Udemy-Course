row1 = ["O", "O", "O"]
row2 = ["O", "O", "O"]
row3 = ["O", "O", "O"]

map1 = [row1, row2, row3]

treasure = int(input("Where do you want to put the treasure?"))

print(f"{row1}\n{row2}\n{row3}\n")

horizontal = int(treasure[0])
vertical = int(treasure[1])

print(map1[vertical])


