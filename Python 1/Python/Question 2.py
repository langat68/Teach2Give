'''Question 2: Fibonacci Sequence 
Write a program to generate the Fibonacci sequence up to 100.
Start of the solution '''

 #Function to generate sequence up to a given limit
def fibonacci_sequence(limit):
    #initilaising variables for the first 2 numbers
    sequence = [0, 1]

    #loop top generate Fibbonacci sequence up to the limit
    while sequence[-1] + sequence[-2] <= limit:
        #adding sequence to the list
        sequence.append(sequence[-1] + sequence[-2])
    return sequence


#Set limit for the Fibbonacci sequence
fib_sequence = fibonacci_sequence(100)

#call the function to generate Fibbonacci sequence to the limit
print(fib_sequence)
