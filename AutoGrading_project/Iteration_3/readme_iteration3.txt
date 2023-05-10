Gist of this iteration:
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