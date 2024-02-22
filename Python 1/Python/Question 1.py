''' Question 1: FizzBuzz
Write a program that prints the numbers from 1 to 100. For multiples of 3, print "Fizz"; for 
 multiples of 5, print "Buzz"; and for numbers that are multiples of both 3 and 5, print 
"FizzBuzz". '''
#loop through numbers from 1 to 100

for i in range(1, 101):
    # check if the number is divisible by both 3 and 5
    if i % 3 == 0 and i % 5 == 0:
        #if divisible by both 3 and 5,print "FizzBuzz"
        print("FizzBuzz")
    #check if the number is divisible by 3
    elif i % 3 ==0:
        #If divisible by 3, print "Fizz"
        print("Fizz")
    #check if number is divisible by 5, print "Buzz"    
    elif i % 5 == 0:
        #if not divisible by 5,print "Buzz"
        print("Buzz")
    else:
        #If not divisible by either 3 or by 5,print the number itself
        print(i)
