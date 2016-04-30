Evaluation Script

There are total 3 scripts for different purposes:
1.	Evaluation-script.py (python V 3.0)
2.	Eval-script-v2.7.py (python V 2.7)
3.	Evaluation-script-batch-mode.py (Batch mode evaluation)

Run command:

> eval-script-name.py path-of-result-data-file

[path-of-result-data-file is path to output file from CRF tool]

Program setup:

•	Set annotation_path variable in the code. (This is the path to the annotated file to be compared with CRF results / Development data file)
 
Note: 

•	Both these files needs to be in CONELL format and last column should be True/False.
•	You may have to change index values of data structures (annotation_line_tokens, crf_line_tokens) based on the number of feature columns in input files.

