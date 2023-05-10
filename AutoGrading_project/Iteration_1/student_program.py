import sys

# Check if the input file is provided as a command line argument
if len(sys.argv) < 2:
    print("Input file not provided.")
    sys.exit(1)

# Read the input file name from the command line argument
input_file = sys.argv[1]

try:
    with open(input_file, 'r') as file:
        # Read each line from the input file
        for line in file:
            # Remove leading/trailing whitespaces and newline characters
            line = line.strip()

################ WRITE YOUR CODE HERE ####################################   
            # Convert the line to a list of numbers
            numbers = [int(num) for num in line.split()]

            # Compute the sum of numbers except the last one
            total_sum = sum(numbers[:-1])

            # Print the sum
            print(total_sum)

################ YOUR CODE ENDS HERE #################################### 

except FileNotFoundError:
    print("File not found:", input_file)


