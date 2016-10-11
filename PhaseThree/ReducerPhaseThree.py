#!/usr/bin/env python
from __future__ import division
import sys

# TF-IDF computation: Phase Three
# Reducer output: <<word, document_name> tf-idf>
NUM_DOCUMENTS = 9
DOC_NAME_IDX = 0
WORD_COUNT_IDX = 1
WORDS_IN_DOC_IDX = 2

corpus_word_count = 0
old_word = None
word_stats_dict = {}
corpus_word_count_dict = {}

for line in sys.stdin:
    line = line.rstrip()
    (word, val) = line.split('\t', 1)
    word_stats = val.split(',')
    count = word_stats[3]

    if old_word != word:
        if old_word:
            corpus_word_count_dict[old_word] = corpus_word_count
            corpus_word_count = 0
        old_word = word
    try:
        corpus_word_count += int(count)
        if word in word_stats_dict.keys():
            word_stats_dict[word].append(word_stats[DOC_NAME_IDX] + "," + word_stats[WORD_COUNT_IDX] + ","
                                         + word_stats[WORDS_IN_DOC_IDX])
        else:
            word_stats_dict[word] = list()
            word_stats_dict[word].append(word_stats[DOC_NAME_IDX] + "," + word_stats[WORD_COUNT_IDX] + ","
                                         + word_stats[WORDS_IN_DOC_IDX])
    except:
        continue
corpus_word_count_dict[old_word] = corpus_word_count



# Computing TF-IDF
for word in corpus_word_count_dict.keys():
    word_stats_list = word_stats_dict[word]
    for word_stats in word_stats_list:
        word_stats = word_stats.split(",")
        try :
          term_frequency = int(word_stats[WORD_COUNT_IDX])/int(word_stats[WORDS_IN_DOC_IDX])
          inverse_doc_freq = NUM_DOCUMENTS / corpus_word_count_dict[word]
          tf_idf = term_frequency * inverse_doc_freq
          print_key = word + "," + word_stats[DOC_NAME_IDX]
          print "%s\t%s" % (print_key, tf_idf)
        except ZeroDivisionError as ex:
          print word_stats[WORDS_IN_DOC_IDX]
          print "Error", ex

