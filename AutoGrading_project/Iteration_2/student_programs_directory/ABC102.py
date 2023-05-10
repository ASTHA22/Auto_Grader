
####################################################################################
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

            # Convert the line to a list of numbers
            numbers = [int(num) for num in line.split()]

############## WRITE YOUR CODE HERE ####################################            
            # Compute the sum of numbers except the last one
            total_sum = sum(numbers[:])

            # Print the sum
            print(total_sum)
############## END YOUR CODE HERE ####################################

except FileNotFoundError:
    print("File not found:", input_file)
