import random

answer = input(str("Please enter the user's names seperated by commas"))
partitions = answer.split(",")

randomNum = random.randint(0, (len(partitions) - 1))

print(partitions[randomNum]+" Was Picked")



