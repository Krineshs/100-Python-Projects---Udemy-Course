print("Welcome to Treasure Island")
print("Your Mission is to find the treasure.")
crossRoad = input("You're at a cross road. Where do you want to go? Type ""Left"" or ""Right"" ")

if crossRoad == "Left":
    island = input(
        "You come to a lake. There is an island in the middle of the lake. Type ""Wait"" to wait for a boat. Type ""Swim"" to swim accross")

    if island == "Wait":
        door = input(
            "You arrive at the island unharmed. There is a house with 3 doors. One Red, One Yellow and One Blue. "
            "Which colour do you choose?")

        if door == "Yellow":
            print("You Win")
        else:
            print("Game Over")
    else:
        print("Game Over")
else:
    print("Game Over")
