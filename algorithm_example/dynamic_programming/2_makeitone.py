# Only these operations are possible for a given integer x : 1~3) If X is divided by 5 or 3 or 2, Divide X by 5 or 3 or 2.     4) X - 1
# Make a integer(X) 1 using these operations and find the minimum number of operations
# Input Example 26  Output 3

# My solution  -----------> Not yet solved
x =  int(input())

d = [0] * 30001

dividers = [5,3,2]

for i in range(1, x+1, 1):
    count = 0
    while (i != 1):
        if d[i] != 0:
            count += d[i]
            break
        
        elif (i % 2 == 0) or (i % 3 == 0) or (i % 5 == 0):
            for divider in dividers:
                if i % divider == 0:
                    i = i // divider
                    count += 1
                    break
         
        else:
            i = i - 1
            count += 1
    
    d[i] = count

print(d[x])

'''
# The model solution
x = int(input())

d = [0] * 30001

for i in range(2, x + 1):
    d[i] = d[i - 1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5] + 1)

print(d[x])
'''