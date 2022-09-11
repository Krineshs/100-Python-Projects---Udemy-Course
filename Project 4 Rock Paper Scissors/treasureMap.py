row1 = ["O", "O", "O"]
row2 = ["O", "O", "O"]
row3 = ["O", "O", "O"]

treasure = int(input("Where do you want to put the treasure?"))

x = treasure[1]
y = treasure[0]

row1 = row1[x] - 1

print(f"{row1}")
