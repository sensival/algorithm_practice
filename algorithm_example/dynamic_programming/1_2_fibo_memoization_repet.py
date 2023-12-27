# Initialize the list for once-calculated results to be memoized
d = [0] * 100

# The 1st and 2nd Fibonacci numbers are 1
d[1] = 1
d[2] = 1
n = 99

# Implement Fibonacci functions using repetitive functions ---> Bottom-up
for i in range(3, n+1):
    d[i] = d[i-1]+d[i-2]

print(d[n])