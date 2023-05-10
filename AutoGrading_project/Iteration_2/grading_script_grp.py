import sys
import subprocess
import os
import csv

# Check if the correct number of command-line arguments are provided
if len(sys.argv) < 3:
    print("Usage: python grading_script_grp.py <student_programs_directory> <test_cases.txt>")
    sys.exit(1)

student_programs_directory = sys.argv[1]
test_cases_file = sys.argv[2]

# Read the test cases from the file

with open(test_cases_file, 'r') as file:
    test_cases = file.readlines()

# Remove leading/trailing whitespaces and newline characters from test cases
test_cases = [test_case.strip() for test_case in test_cases]

results = {}

# Iterate over student programs in the directory
for filename in os.listdir(student_programs_directory):
    if filename.endswith(".py"):
        student_program = os.path.join(student_programs_directory, filename)

        # Initialize pass_flag for each student program
        pass_flag = 0

        # Iterate over test cases
        for i, test_case in enumerate(test_cases):
            # Split the test case into individual values
            values = test_case.split()

            # Run the student program with the current test case input
            process = subprocess.Popen(['python', student_program, test_cases_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)            
            stdout, stderr = process.communicate()

            # Check if there was an error executing the student program
            if stderr.strip():
                print(f"Error executing {student_program}: {stderr.strip()}")
                break

            # Parse the student output and check the test case result
            try:
                expected_output = int(values[-1])
                student_output = [int(x) for x in stdout.strip().split()]

                if student_output[i] == expected_output:
                    pass_flag += 1
            except ValueError:
                print(f"Invalid output format from {student_program}: {stdout.strip()}")
                break

        else:
            # Calculate the percentage of pass cases
            total_cases = len(test_cases)
            pass_percentage = (pass_flag / total_cases) * 100 if total_cases > 0 else 0

            # Store the results
            results[filename] = {
                'Pass cases': pass_flag,
                'Fail cases': total_cases - pass_flag,
                'Pass percentage': pass_percentage
            }

# Write the results to a CSV file
output_file = 'results.csv'
with open(output_file, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Student Program', 'Pass cases', 'Fail cases', 'Pass percentage'])
    writer.writeheader()
    for filename, result in results.items():
        writer.writerow({
            'Student Program': filename,
            'Pass cases': result['Pass cases'],
            'Fail cases': result['Fail cases'],
            'Pass percentage': result['Pass percentage']
        })

print("Grading completed. Results written to", output_file)
