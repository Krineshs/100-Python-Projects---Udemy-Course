print("Welcome to the tip Calculator")

totalBill = float(input("What was the total bill? $"))
percentageTip = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
peopleSplit = int(input("How many people to split the bill?"))

totaltip = float(totalBill/percentageTip)
payEach = float((totaltip+totalBill)/peopleSplit)
total = "{:.2f}".format(payEach)

print(f"Each Person should pay: ${total}")


