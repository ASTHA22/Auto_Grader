# Auto_Grader
This project is used to grade the python codes and test on different test case scenarios

The autograding project has 4 iterations:

**Iteration 1:**
Detailed output of the individual student programs can be checked using this iteration for each test case instance.
The student needs to write code in give block in student program base code.
The grading works for test cases with integer or numerical inputs and outputs.
Hence, we can check how many test cases does the program pass and fail and it's respective details.

Iteration_1 folder has following files:
1. test_cases.txt - Test cases file where last column is expected output
2. student_program.py - Program submitted by the student. Student must write their codes in the given block only
3. grading_script.py - this code runs the test cases on the student program and gives test case - pass/fail results and an overall summary. It generates a result.csv output
4. result.csv - This file is generated after running the command in the terminal. The file will contain details for each test case instances and an overall summary.
Result file will be stored in the default Jupyter folder. If you want to change it to custom path then change line 52 of 'grading_script.py' code to : csv_file = '/path/to/results.csv'
Eg: csv_file = 'Documents/results.csv'

Run the following command in Jupyter terminal:
python /path/to/grading_script.py  /path/to/student_program.py /path/to/test_cases.txt
Eg:
python /Users/asthasingh/AutoGrading_project/Iteration_1/grading_script.py /Users/asthasingh/AutoGrading_project/Iteration_1/student_program.py /Users/asthasingh/AutoGrading_project/Iteration_1/test_cases.txt

**Iteration 2:**
Takes all the student programs and generates an overall report for each student program level details of pass cases, fail cases and pass % for each student.
The student needs to write code in give block in student program base code.
The grading works for test cases with integer or numerical inputs and outputs.
Hence, we can get student level test case pass % and can grade relatively based on it.

Iteration_2 folder has following files/folders:
1. test_cases.txt - Test cases file where last column is expected output
2. student_programs_directory folder - has all the python codes submitted by students. The name of the file should be NetId of the student. Student must write their codes in the given block only
3. grading_script_grp.py - this code runs the test cases on all the student program codes and gives test results. It generates a result.csv output
4. result.csv - This file is generated after running the command in the terminal. The result file will have student level test case pass cases, fail cases and pass %.
Result file will be stored in the default Jupyter folder. If you want to change it to custom path then change line 70 of 'grading_script_grp.py' code to : output_file = '/path/to/results.csv'
Eg: output_file = 'Documents/Grader_project/results.csv'

Run the following command in Jupyter terminal:
python /path/to/grading_script_grp.py /path/to/student_programs_directory /path/to/test_cases.txt
Eg:
python /Users/asthasingh/AutoGrading_project/Iteration_2/grading_script_grp.py /Users/asthasingh/AutoGrading_project/Iteration_2/student_programs_directory /Users/asthasingh/AutoGrading_project/Iteration_2/test_cases.txt

**Iteration 3:**
This iteration is more suitable for complex student programs like big data assignment codes.
The student need not write code in the specified block unlike iteration 1&2, students can submit their code as it is. The test case file should be expected output file.
This iteration checks the student program's output to the expected output file and gives the result for the matches and mismatches in the actual and expected outputs.
Hence, we can check how much does the actual output matches the expected output and detect the discrepancies in the outputs.

Iteration_3 folder has following files:
1. test_bigdata_hw3_q1_p1.txt - Expected output file
2. student_program_bd_hw3_q1_p1.py - Program submitted by the student. The student need not write code in the specified block unlike iteration 1&2, students can submit their code as it is.
3. grading_script_bd_s.py - This code checks the student program's output to the expected output file and gives the result for the matches and mismatches in the actual and expected outputs and an overall summary. It generates a result.csv output
4. result.csv - This file is generated after running the command in the terminal. The file will contain details of actual output and expected output, match/mismatch and an overall summary.
Result file will be stored in the default Jupyter folder. If you want to change it to custom path then change line 72 of 'grading_script_bd_s.py' code to : csv_file = '/path/to/results.csv'
Eg: csv_file = 'Documents/results.csv'

Run the following command in Jupyter terminal: python grading_script_bd_s.py <student_program.py> <test_cases.txt>
python /path/to/grading_script_bd_s.py  /path/to/student_program_bd_hw3_q1_p1.py /path/to/test_bigdata_hw3_q1_p1.txt
Eg:
python /Users/asthasingh/AutoGrading_project/Iteration_3/grading_script_bd_s.py /Users/asthasingh/AutoGrading_project/Iteration_3/student_program_bd_hw3_q1_p1.py /Users/asthasingh/AutoGrading_project/Iteration_3/test_bigdata_hw3_q1_p1.txt

Note: The example used here for grading is of big data hw3 q1 part 1

**Iteration 4:**
This iteration is more suitable for complex student programs like big data assignment codes.
It takes all the student programs and generates an overall report for each student program level details of pass cases, fail cases and pass % for each student.
The student need not write code in the specified block unlike iteration 1&2, students can submit their code as it is. The test case file should be expected output file.
Hence, we can get student level match % with respect to the expected output for each student and can grade relatively based on it.

Iteration_4 folder has following files/folders:
1. test_bigdata_hw3_q1_p1.txt - Expected output file
2. prog_dir folder - has all the python codes submitted by students. The name of the file should be NetId of the student. The student need not write code in the specified block unlike iterations 1 & 2, students can submit their code as it is.
3. grading_script_bd_grp.py - This code runs the all the student programs and checks each student program's output to the expected output file and gives the result for the match/mismatch and match % with respect to the expected output for each student and an overall summary. It generates a result.csv output
4. result.csv - This file is generated after running the command in the terminal. The file will contain details of actual output and expected output, match/mismatch, match % at each student program level and an overall summary.
Result file will be stored in the default Jupyter folder. If you want to change it to custom path then change line 60 of 'grading_script_grp.py' code to : csv_file = "grading_results.csv"
Eg: csv_file = 'Documents/Grader_project/grading_results.csv'

Run the following command in Jupyter terminal: python grading_script_bd_grp.py <student_programs_directory> <test_cases.txt>

python /path/to/grading_script_bd_grp.py /path/to/prog_dir /path/to/test_bigdata_hw3_q1_p1.txt
Eg:
python /Users/asthasingh/AutoGrading_project/Iteration_4/grading_script_bd_grp.py /Users/asthasingh/AutoGrading_project/Iteration_4/prog_dir /Users/asthasingh/AutoGrading_project/Iteration_4/test_bigdata_hw3_q1_p1.txt

Note: The example used here for grading is of big data hw3 q1 part 1
