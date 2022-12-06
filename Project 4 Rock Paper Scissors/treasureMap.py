row1 = ["O", "O", "O"]
row2 = ["O", "O", "O"]
row3 = ["O", "O", "O"]

map1 = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

treasure = input("Where do you want to put the treasure?")

horizontal = int(treasure[0])
vertical = int(treasure[1])

row = map1[vertical - 1][horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")





