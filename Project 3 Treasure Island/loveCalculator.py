print("Welcome to the love Calculator")

name = str(input("What is your name?")).lower()
name2 = str(input("What is their name?")).lower()

T = name.count("t") + name2.count("t")
R = name.count("r") + name2.count("r")
U = name.count("u") + name2.count("u")
E = name.count("e") + name2.count("e")
L = name.count("l") + name2.count("l")
O = name.count("o") + name2.count("o")
V = name.count("v") + name2.count("v")
E = name.count("e") + name2.count("e")

true = T + R + U + E
love = L + O + V + E
print(f"{true}{love}%")
