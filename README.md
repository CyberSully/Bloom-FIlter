# Hashshield Bloom Filter Program

This project is a Python implementation of a Bloom Filter, a probabilistic data structure used for fast membership testing with controlled false positives. The Bloom Filter in this project tests membership of items in a large dataset efficiently. It’s commonly applied in scenarios like password checks, blacklist filters, and spell-checking.

In this implementation, two datasets are used: rockyou.ISO-8859-1.txt as a large dataset of common passwords to load into the Bloom Filter, and dictionary.txt to test membership. The program calculates statistics such as true positives, false positives, true negatives, and false negatives.

To set up, ensure Python 3 is installed with the bitarray and mmh3 libraries. Install these by running pip install bitarray mmh3. Place rockyou.ISO-8859-1.txt and dictionary.txt in the same directory as bloomy.py and run the program with python bloomy.py.

The program initializes the Bloom Filter, loads the rockyou.ISO-8859-1.txt data, and tests each word in dictionary.txt for membership. It outputs statistics and performance timings, showing the true positive, false positive, true negative, and false negative rates.

A Bloom Filter is memory-efficient and fast, suitable for large datasets. However, it has a small false-positive rate, meaning it might incorrectly flag an item as present. For a deeper understanding, consult resources like Geeks for Geeks - Bloom Filters and Molecular Sciences - Implementing a Bloom Filter.
