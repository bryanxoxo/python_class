# Challenge: To Create a function called uppercase_and_reverse that takes a little bit of text, uppercases it all, 
# and then resverses it (flips all the letters around)
def uppercase_and_reverse(text):
	modified_text=text[::-1]
	return modified_text.upper()

text = "Lauren's name"

print(text)

fuckall=input("Enter the string:")

#fuckthis=input("tell me wher to fuck off:")
print(f"This is something {text} ", uppercase_and_reverse(fuckall))

#print(uppercase_and_reverse(fuckthis))