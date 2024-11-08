from bitarray import bitarray
import mmh3

class BloomFilter:
    # call to create new bloomfilter
    def __init__(self, size, hash_count):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)
    # adds element to bloom
    def add(self, item):
        for seed in range(self.hash_count):
            index = mmh3.hash(item, seed) % self.size
            self.bit_array[index] = 1

    def contains(self, item):
    # checks bloom for contents
        for seed in range(self.hash_count):
            index = mmh3.hash(item, seed) % self.size
            if self.bit_array[index] == 0:
                return False
        return True

def main():
    print("Initializing Bloom Filter...")
    bloom_filter_size = 1000000  # Adjusted bloom filter size for better performance
    hash_functions_count = 5
    bloom_filter = BloomFilter(bloom_filter_size, hash_functions_count)

    print("Loading data into Bloom Filter from rockyou.txt...")
    try:
        with open('rockyou.ISO-8859-1.txt', 'r', encoding='latin-1') as f:
            for line in f:
                bloom_filter.add(line.strip())
    except FileNotFoundError:
        print("Error: File 'rockyou.ISO-8859-1.txt' not found.")
        return

    print("Testing data from dictionary.txt...")
    true_positive = 0
    false_negative = 0

    try:
        with open('dictionary.txt', 'r', encoding='latin-1') as f:
            for line in f:
                word = line.strip()
                if bloom_filter.contains(word):
                    true_positive += 1
                else:
                    false_negative += 1
    except FileNotFoundError:
        print("Error: File 'dictionary.txt' not found.")
        return

    # Calculating statistics
    total_words = true_positive + false_negative
    false_positive = bloom_filter_size - true_positive
    try:
        with open('dictionary.txt', 'r', encoding='latin-1') as f:
            true_negative = len(f.readlines()) - total_words - false_positive
    except FileNotFoundError:
        print("Error: File 'dictionary.txt' not found.")
        return

    print("True positive:", true_positive)
    print("False positive:", false_positive)
    print("True negative:", true_negative)
    print("False negative:", false_negative)

if __name__ == "__main__":
    main()
