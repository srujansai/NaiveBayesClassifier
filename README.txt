

nbtrain.py

GIVEN: The complete path that contains the training data (directory that has pos and neg sub directories) and a output file.
RETURNS: A text file as given output file above but with model data containing pos, neg and complete vocab dictionary.

nbtest.py

GIVEN: A model file, the complete path that contains the testing data (directory that has text files within) and a output file.
RETURNS: 
1) A prediction file for the above testing data containing scores the model assigns to the possibilities of positive and negative reviews, as an output file.
2) File containing 20 terms with highest (log) ratio of positive to negative weight
3) File containing 20 terms with highest (log) ratio of negative to positive weight



 