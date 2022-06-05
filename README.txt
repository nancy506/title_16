This project is an assignment for job interview.
The goal is to read a corpus and retrieve useful information from such corpus


To run title_16_update.py:
1. Install python3 
2. Put title_16.json data file in working directionary
3. For Mac user: Type python3.6 title_16_update.py in terminal

Output:
1.ngrams.txt: a corpus of all ngrams contained in the json file
2.ngram_frequency.txt: The frequency of each ngram in the corpus
3.ngram_probability.txt:The probability of each ngram in the corpus
4.ngram_entropy.txt: The entropy of each ngram in the corpus


Some notes:
1. An alternative way of tokenizing is to use natural language toolkit. To remain consistency, I chose to use self-defined method for all tasks in this file.
2. The value of entropy depends on the definition of it. one can also define entropy as the sum of entropy of each character contained in the ngram. For simplicity sake, I chose not to do so.
3. The tokenization of sentences need to be improved.  Abbreviation mark, for example, are recognized as delimiters too. However, due to time constraint, I skipped that part.

