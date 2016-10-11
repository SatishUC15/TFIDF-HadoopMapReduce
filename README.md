# TFIDF-Hadoop

Implementation of TFIDF in Hadoop using Python as three phases. 

Phase 1:
-------
  Mapper: ((word, doc_id), 1)
  
  Reducer: ((word, doc_id), word_count_in_doc)

Phase 2:
-------
  Mapper: (doc_id, (word, word_count_in_doc))
  
  Reducer: ((word, doc_id), (word_count_in_doc, words_in_doc))

Phase 3:
-------
  Mapper: (word, (doc_id, word_count_in_doc, words_in_doc, 1))
  
  Reducer: ((word, doc_id), tf-idf)

The mapper and reducer programs associated with each phase, and the output files are available in the repository.


Hadoop commands:
=====================
To test via pipes: cat Data/* | ./MapperPhaseOne.py | sort | ./ReducerPhaseOne.py

To run on cluster: hadoop jar /root/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar -input <input directory> -output <output directory> -file *.py -mapper MapperPhaseOne.py -reducer ReducerPhaseOne.py
