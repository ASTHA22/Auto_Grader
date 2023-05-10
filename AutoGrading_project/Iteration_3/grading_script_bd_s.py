import sys
import subprocess
import csv

# Check if the correct number of command-line arguments are provided
if len(sys.argv) < 3:
    print("Usage: python grading_script_bd_s.py <student_program.py> <test_cases.txt>")
    sys.exit(1)

student_program = sys.argv[1]
test_cases_file = sys.argv[2]

# Read the test cases from the file
with open(test_cases_file, 'r') as file:
    test_cases = file.readlines()

# Remove leading/trailing whitespaces and newline characters from test cases
test_cases = [test_case.strip() for test_case in test_cases]

# Run the student program with the test case file as input
process = subprocess.Popen(['python', student_program, test_cases_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
stdout, stderr = process.communicate()

student_output = stdout.strip()

student_output_lines = student_output.split('\n')

results = []

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
        test_case_result = "Pass"
        pass_flag += 1
    else:
        test_case_result = "Fail"

    # Store the test case result in the results list
    results.append({
        'Test case num': i,
        'Expected Output': expected_output,
        'Student Output': student_output_formatted,
        'Test case result': test_case_result
    })

print("Pass cases:", pass_flag)
print("Fail cases:", len(test_cases) - pass_flag)

# Calculate pass percentage
total_cases = len(test_cases)
pass_percentage = (pass_flag / total_cases) * 100 if total_cases > 0 else 0

# Add summary to results list
summary = {
    'Test case num': 'Summary',
    'Expected Output': f"Pass cases: {pass_flag}",
    'Student Output': f"Fail cases: {len(test_cases) - pass_flag}",
    'Test case result': f"Pass percentage: {pass_percentage:.2f}%"
}
results.append(summary)

# Write the results to a CSV file
output_file = 'results.csv'
with open(output_file, 'w', newline='') as file:
    fieldnames = ['Test case num', 'Expected Output', 'Student Output', 'Test case result']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(results)

print("Grading completed. Results written to", output_file)
