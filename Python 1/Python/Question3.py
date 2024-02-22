'''Question 3: Power of Two
Write a program that takes an integer as input and returns true if the input is a power of two.
Examples: 
8=> returns true
6=> returns false
'''

def is_power_of_two(num):

#Function to check if a number is a power of two.
    
    
    # Check if num is greater than 0 and if it has only one bit set to 1
    return num > 0 and (num & (num - 1)) == 0

# Taking input from the user
num = int(input("Enter an integer: "))

# Checking if the input number is a power of two
result = is_power_of_two(num)

# Printing the result 
#Returns bool,True if sum is a power of two,False otherwise
print(f"{num} is a power of two: {result}")
