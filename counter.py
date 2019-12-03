import sys
import pandas as pd
from nltk import word_tokenize
import re
import string

# Set variables for the input and output files
input_file = sys.argv[1]
output_file = sys.argv[2]

# Read in the text file
print(f'Reading {input_file}...')
f = open(input_file, encoding="utf8")

# Read in the data
text = f.read()

# Remove capitals
text = text.lower()

# Remove punctuation marks
for punctuation_mark in string.punctuation:
    text = text.replace(punctuation_mark, '')

# Tokenize
words = word_tokenize(text)
word_series = pd.Series(words)

# Remove spaces
word_series = word_series.apply(lambda x: x.replace(' ', '')).copy()

# Count the words!
word_counts = word_series.value_counts()

# Set this into a dataframe
word_counts_df = pd.DataFrame(word_counts).reset_index()
word_counts_df.columns = ['word', 'count']

# Write out the word counts to a csv file
print(f'Writing to csv...')
word_counts_df.to_csv(output_file, index=False)
