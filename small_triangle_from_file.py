import csv  # Importing csv module to read the file
with open('small_triangle.csv') as p:
    # Creating list of lists to form the pyramid from the read dataset.
    triangle = [list(map(int, rec)) for rec in csv.reader(p, delimiter=',')]

# Creating list of prime numbers until 1000 (The largest value in dataset is 999)
primes = [i for i in range(2, 1000) if 0 not in [i % n for n in range(2, i)]]

# Replacing prime numbers with a large negative number to make sure
# that path with the highest sum won't be a path involving prime number(s).
for prime_num in primes:
    for i, x in enumerate(triangle):
        for j, a in enumerate(x):
            if triangle[i][j] == prime_num:
                triangle[i][j] = -32000


# Function to find the path with the highest sum from bottom to the top.
def find_path():
    for i in reversed(range(len(triangle) - 1)):
        for j in range(len(triangle[i])):
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])
    return str(triangle[0][0])


print(find_path())
