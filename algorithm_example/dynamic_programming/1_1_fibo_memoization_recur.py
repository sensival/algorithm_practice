# Initialize the list for once-calculated results to be memoized
d = [0] * 100

# Implement Fibonacci functions using recursive functions---> Top-down, Time complexity O(n)
def fibo(x):
    print('f(' + str(x) + ')')
    # Return 1 when 1 or 2
    if x ==1 or x == 2:
        return 1
    # if it is once-calculated results, return them
    if d[x] != 0:
        return d[x]
    
    # if it is not calculated yet, return the Fibonacci result 
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))