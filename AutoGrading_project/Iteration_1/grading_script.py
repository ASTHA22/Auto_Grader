import sys
import csv
import subprocess

# Check if the correct number of command-line arguments is provided
if len(sys.argv) < 3:
    print("Usage: python grading_script.py <student_program.py> <test_cases.txt>")
    sys.exit(1)

student_program = sys.argv[1]
test_cases_file = sys.argv[2]

# Read the test cases from the file
with open(test_cases_file, 'r') as file:
    test_cases = file.readlines()

# Remove leading/trailing whitespaces and newline characters from test cases
test_cases = [test_case.strip() for test_case in test_cases]

expected_output = []

# Run the student program with the test case file as input
process = subprocess.Popen(['python', student_program, test_cases_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
stdout, stderr = process.communicate()
student_output = [int(x) for x in stdout.strip().split()]

# Iterate over test cases
results = []
pass_flag = 0

for i, test_case in enumerate(test_cases):
    # Split the test case into individual values
    values = test_case.split()

    # Store the student output and expected output
    expected_output.append(int(values[-1]))

    # Check the test case result
    if student_output[i] == expected_output[i]:
        result = "Pass"
        pass_flag += 1
    else:
        result = "Fail"

    # Add the result to the results list
    results.append((i, expected_output[i], student_output[i], result))

# Calculate pass percentage
pass_percentage = (pass_flag / len(expected_output)) * 100

# Write results to a CSV file
csv_file = 'results.csv'
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Test case num", "Expected Output", "Student Output", "Result"])
    writer.writerows(results)
    writer.writerow([])  # Add an empty row
    writer.writerow(["Expected output:"] + expected_output)
    writer.writerow(["Student output:"] + student_output)
    writer.writerow(["Pass cases:", pass_flag])
    writer.writerow(["Fail cases:", len(expected_output) - pass_flag])
    writer.writerow(["Pass percentage:", f"{pass_percentage:.2f}%"])

# Print summary
print("Expected output:", expected_output)
print("Student output:", student_output)
print("Pass cases:", pass_flag)
print("Fail cases:", len(expected_output) - pass_flag)
print("Pass percentage:", f"{pass_percentage:.2f}%")
print("Results written to", csv_file)
