import sys
import subprocess
import glob
import csv

# Check if the correct number of command-line arguments are provided
if len(sys.argv) < 3:
    print("Usage: python grading_script_bd_grp.py <student_programs_directory> <test_cases.txt>")
    sys.exit(1)

student_programs_directory = sys.argv[1]
test_cases_file = sys.argv[2]

# Get a list of all Python files in the directory
student_programs = glob.glob(student_programs_directory + "/*.py")

# Read the test cases from the file
with open(test_cases_file, 'r') as file:
    test_cases = file.readlines()

# Remove leading/trailing whitespaces and newline characters from test cases
test_cases = [test_case.strip() for test_case in test_cases]

results = []

# Iterate over student programs
for student_program in student_programs:
    # Run the student program with the test case file as input
    process = subprocess.Popen(['python', student_program, test_cases_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate()

    student_output = stdout.strip()

    student_output_lines = student_output.split('\n')
    # Iterate over test cases and student output lines simultaneously
    pass_flag = 0
    for i, (expected_output, student_output) in enumerate(zip(test_cases, student_output_lines)):
        # Split the student output line into individual values
        student_output_values = student_output.strip().split('|')
        student_output_formatted = '|'.join(student_output_values)  # Join values with '|'

        # Split the expected output line into individual values
        expected_output_values = expected_output.strip().split('|')

        # Check the test case result
        if student_output_values == expected_output_values:
            pass_flag += 1

    # Calculate pass and fail cases
    pass_cases = pass_flag
    fail_cases = len(test_cases) - pass_flag

    # Calculate the percentage of pass cases
    pass_percentage = (pass_cases / len(test_cases)) * 100

    # Append results to the list
    results.append((student_program, pass_cases, fail_cases, pass_percentage))

# Write the results to a CSV file
csv_file = "grading_results.csv"
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Student Program", "Pass Cases", "Fail Cases", "Pass Percentage"])
    writer.writerows(results)

print("Grading results saved to", csv_file)
