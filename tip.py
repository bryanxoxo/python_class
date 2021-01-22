#here I am printing some basic output for the user to set the scene!
print("Wow what a yummy meal. It looks like the waiter is coming with the check.")
print("I'm having trouble reading that without my glasses, can you take a look?")
print("")

#I'm setting the bill_amount as a string by grabbing the input from the user.
bill_amount = (input("Tell me, What is the total of the bill?"))

#here we are looking for the string to see if it has a $ and then using the replace function to remove it and assign it to a new string called converted_bill_amount
converted_bill_amount = bill_amount.replace("$", "")

#here we are using the float function to convert the bill into an number we can use to mulitply against.
Int_converted_bill_amount = float(converted_bill_amount)

#These are the strings for each tip choice, 15%, 18%, and 20%.
tip_15 = Int_converted_bill_amount * .15
tip_18 = Int_converted_bill_amount * .18
tip_20 = Int_converted_bill_amount * .20

#Finally we are printing the output of the above math and assigning the last 2 digits of the float to properly display any cents.
print("")
print(f"Sounds like your tip should be {tip_15:.2f}, if you are cheap; {tip_18:.2f}, if you are generous; or {tip_20:.2f} if you appreciate the service industry.")
