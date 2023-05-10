Gist of this iteration:
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