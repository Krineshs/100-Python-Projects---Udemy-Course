import random

answer = input(str("Please enter the user's names seperated by commas"))
partitions = answer.split(",")

randomNum = random.randint(1, len(partitions))

print(partitions[randomNum])



