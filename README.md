# external-search

This is a small code in Python, to reproduce the "external-search" approach.
With this code, you can sort a large file, on a low memory machines.

I need to be honest, this Python script is too far from the best performance benchmark, but it works fine.

## Scripts details

**create_test_file.sh**

This shell script calls a ruby routine that creates a large text file (5 million lines). Each line has 16 words, got by randomizing words from the "/usr/share/dict/words" reference file.
The created file is called "file.txt".

**external_search.py** 

This Python script uses the "file.txt" input file, and generates the "file_py_out.txt" output sorted file. The script works spliting the input file, in some temp sorted files (100000 lines per temp file). Finaly the script merges all the temp files, applying another step of sorting.

Thanks,  
Ernesto
