#Fizzbuzz is an infamous challenge used as an interview question during hiring. With the knowledge we have we can answer the fizzbuzz challenge. 


#Write a program that prints the numbers form 1 to 100
#But for multiples of three print "fizz" instead of the number
#for Multiples of 5 print "buzz". 
# for multiples of both three and five print "fizz-buzz"

#hint: % (modulo) tells you what's left over when you divide one nmumber by another
# ex. number % 3 == 0


#first let's set our number variable loop with the range 1-100
for number in (range(1,101)):

	if number % 3 == 0 and number % 5 == 0:
		print("fizz-buzz")
	elif number % 5 == 0:
		print("buzz")
	elif number % 3 == 0: 
		print("fizz")
	else:
		print(number)