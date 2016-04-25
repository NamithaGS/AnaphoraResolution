How to run the program:
Replace the "foldername" variable in the candidateSelection.py file to the folder containing all the manually annotated files.

Output file generated (train_out.txt):
The output file is generated in the following format:

<Annaphora> <candidate> <POS of cand> <Gender Ann> <Gender Can> <Number Ann> <Number Can> <Sentence Distance> <Named Entity> <Person Ann> <Person Cand> <NP Chunk distance> <True/False>


Candidate Selection process involves two steps:

Selection of annaphoras - Since we have already annotated data available, the program selects the annaphoras by picking pronouns with POS tag "PRP" which are at the head of the noun chunk B-NP and which are marked as candidate mentions (the files have candidates and annaphoras marked identically).                         
Candidate Selection - For each annaphora, select all the words which have a POS "NN" or a "NNP" and are present in the current sentence or in the previous 5 sentences relative to the annaphora.


Training:
The candidate selection while training picks candidates between the annaphora and the marked candidate referent.
Testing:
During the development, the candidate selection  picks candidates to the left of the annaphora until 5 previous sentences.


