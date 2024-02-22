
'''
Question 5: Reverse Integer
Write a program that takes an integer as input and returns an integer with reversed digit 
ordering.
Examples:
For input 500, the program should return 5.
For input -56, the program should return -65.
For input -90, the program should return -9.
For input 91, the program should return 19.

'''
def capitalize_words(input_string):
    # Split the input string into words
    words = input_string.split()
    
    # Capitalize the first letter of each word
    capitalized_words = [word.capitalize() for word in words]
    
    # Join the capitalized words back into a string
    result = ' '.join(capitalized_words)
    
    return result

# Test cases
test_strings = ["hi", "i love programming"]
for string in test_strings:
    print(f'Input: "{string}" => Output: "{capitalize_words(string)}"')
