import math

n = 14344383  # Number of elements in rockyou.txt
p = 0.01      # Desired false positive probability

m = int((-n * math.log(p)) / (math.log(2)**2))
print("Recommended Bloom filter size (m):", m)