#!/usr/bin/env python
import sys

# TF-IDF computation: Phase One
# Reducer output: <<word, document_name>   n>

word_count = 0
old_word = None
old_docName = None

for line in sys.stdin:
    (key, val) = line.split('\t', 1)
    (word, doc_name) = key.split(',', 1)

    if old_word != word or old_docName != doc_name:
        if old_word and old_docName:
            print_key = old_word + "," + old_docName
            print '%s\t%s' % (print_key, word_count)
            word_count = 0
        old_word = word
        old_docName = doc_name
    try:
        word_count += int(val)
    except:
        continue
print_key = word + "," + doc_name
print '%s\t%s' % (print_key, word_count)
