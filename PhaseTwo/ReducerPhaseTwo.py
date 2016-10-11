#!/usr/bin/env python
import sys

# TF-IDF computation: Phase Two
# Reducer output: <<word, document_name>   <word_count, word_count_in_document>>

doc_word_count = 0
old_docName = None
doc_words = {}
doc_word_count1 = {}
val = []

for line in sys.stdin:
    line = line.rstrip()
    (doc_name, val) = line.split('\t', 1)
    (word, word_count) = val.split(',', 1)

    if old_docName != doc_name:
        if old_docName:
            doc_word_count1[old_docName] = doc_word_count
            doc_word_count = 0
        old_docName = doc_name
    try:
        doc_word_count += int(word_count)
        if doc_name in doc_words.keys():
            temp_list = doc_words[doc_name]
            temp_list.append(word + "\t" + word_count)
            doc_words[doc_name] = temp_list
        else:
            temp_list = []
            temp_list.append(word + "\t" + word_count) 
            doc_words[doc_name] = temp_list
    except:
        continue
doc_word_count1[old_docName] = doc_word_count

# Generating key-value pairs
for key in doc_words.keys():
    contents = doc_words[key]
    for item in contents:
        item = item.rstrip()
        (word, word_count) = item.split("\t", 1)
        print_key = word + "," + key
        print_value = word_count + "," + str(doc_word_count1[key])
        print '%s\t%s' % (print_key, print_value) 
