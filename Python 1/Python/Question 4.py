'''
Question 4: Capitalize Words
Write a program that accepts a string as input, capitalizes the first letter of each word in the 
string, and then returns the result string.
Examples: 
"hi"=> returns "Hi"
"i love programming"=> returns "I Love Programming"

'''

def capitalise_words(input_string):
    # Split the input string into words
    words = input_string.split()
    
    # Capitalise the first letter of each word
    #converts each word first letter to uppercase
    capitalized_words = [word.capitalize() for word in words]
    
    # Join the capitalised words back into a string
    result = ' '.join(capitalized_words)
    
    #Join the captilised words back into a string 
    #combines the captialized words into a single string with spaces in between 
    
    return result

# Test cases 
#loops the test
test_strings = ["hi", "i love programming"]
for string in test_strings:
    #Print input and output for each test case
    print(f'Input: "{string}" => Output: "{capitalise_words(string)}"')
