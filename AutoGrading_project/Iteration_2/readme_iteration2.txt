Gist of this iteration:
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