#!/usr/bin/env python 
import sys

# TF-IDF computation: Phase Three
# Mapper output: <word, <document_name, word_count, number_of_words_in_document, 1>>

for line in sys.stdin:
    line = line.rstrip()
    (key, value) = line.split('\t', 1)
    (word, doc_name) = key.split(',', 1)
    (word_count, num_words_in_doc) = value.split(',', 1)
    print_value = doc_name + "," + word_count + "," + num_words_in_doc + "," + str(1)
    print '%s\t%s' % (word, print_value)
