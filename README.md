Anaphoric resolution of pronominal entities in Hindi
====================================================



	

> ###INTRODUCTION:


Anaphora is an expression whose interpretation is dependent upon another expression in context. When two or more expressions in a text refer to the same person or thing; they have the same [referent](https://en.wikipedia.org/wiki/Referent) (co-reference), e.g. Bill said he would come; Bill and he refer to the same entity. Anaphoric Resolution is the task of identifying this reference/antecedent.

> ###Challenges faced:



No current state-of-the-art anaphoric resolution system for the Hindi language

Absence of a single standardized, well-annotated corpus and language pre-processing tool for Hindi The structure of the language
-> It does not differentiate pronouns based on gender
-> Honorific references bring further ambiguity

> ###METHOD:

####Materials:

We obtained a Hindi dataset of short news articles from the “Anaphora Resolution for Indian Language”, a tool contest conducted as a part of ICON 2011. This dataset contains three subsets: Development (29 articles), Training (60 articles) and Test (40 stories).

The dataset is presented in column format with relevant pre-processing information.
Fields: File name, line index, word index, word, its POS and chunking information, followed by Named Entity information.

We plan to enrich this data set with the morphological analysis information for each word. We have obtained a tool from the “Indian Language –Indian Language Machine Translation (IL-ILMT)” consortium.

http://www.cfilt.iitb.ac.in/~ilmt/
 

#### Procedure:

We are planning to implement an approach that is based on the paper “A Generic Anaphora Resolution Engine for Indian Languages” (1), a language independent engine.

Key features of this system would be:

 - Shallow Parsing: We perform limited shallow parsing on the training and testing data.

 - Enrich the data using Morphological analysis: The morphological analyzer uses both inflectional and derivational morphology to identify the root word, its lexical category and Person, Noun, Gender (PNG).
 - Two-fold Approach:

	 - Learning Phase:  Use a Rule based algorithm to select the CANDIDATE noun phrases (NP) for a given pronoun. The NPs which agree with the pronoun in PNG should be selected as possible candidates for its antecedent. Here we aim to try and test two different techniques which vary from the paper: 

		 1. Add additional Hindi language specific rules to enable better selection of possible antecedent candidates
		 2. Try out various combinations to decide how many sentences to look ahead for candidate selection.
 
	 Perform a binary classification on each CANDIDATE antecedent to verify whether it is the real antecedent or not. For this task, we will design features to be extracted from the candidate antecedents which are specific to the Hindi language.
	CRFs may be used for learning and identifying the antecedents.


	 - Testing Phase:
	 Use the previously developed model to resolve the entity anaphors present in the test data.

> ###Evaluation:

We have some statistics available from the ICON 2011 dataset. 
We plan to use these numbers to evaluate the performance of our system using measures such as Precision,Recall and F-measure.

> ###REFERENCES

1.	[A Generic Anaphora Resolution Engine for Indian Languages](https://pdfs.semanticscholar.org/c37f/5c59b2539386ada907a1365f5c74ace6e32e.pdf)
2.	[A Hybrid Approach for Anaphora Resolution in Hindi](http://www.aclweb.org/anthology/I13-1130)
3.	[Anaphora resolution in Hindi :Issues and Challenges](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.259.3225&rep=rep1&type=pdf)

