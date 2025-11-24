# Title: Replace Missing Integers to Form Minimum Sum Palindromic Array

# Description:
# The program must accept an array of N integers as input, where some integers are missing and denoted by asterisks (*). You must replace these asterisks with positive integer values so that the array becomes palindromic (reads the same forward and backward) and the sum is minimized. If it is not possible to make the array a palindrome, print -1 as the output. Otherwise, print the resulting palindrome array.

# Boundary Condition(s):

# 1 ≤ N ≤ 100

# 1 ≤ Each integer value ≤ 10^5

# Input Format:

# The first line contains N.

# The second line contains N integers and asterisks separated by a space.

# Output Format:

# The first line contains the palindromic array or -1 based on the given conditions.

# Example Input/Output 1:
# Input:

# text
# 6  
# 10 * 30 30 20 *
# Output:

# text
# 10 20 30 30 20 10
# Explanation:
# Here N = 6.
# To make the array palindrome with the minimum sum, the first asterisk is replaced by 20 and the second asterisk by 10.

# Example Input/Output 2:
# Input:

# text
# 5  
# * 3 * 3 *
# Output:

# text
# 1 3 1 3 1
# Example Input/Output 3:
# Input:

# text
# 7  
# 30 * 10 15 * * 30
# Output:

# text
# -1\

def min_palindrome_array(arr):
    n = len(arr)
    res = arr.copy()
    for i in range(n//2):
        j = n - 1 - i
        # Both are asterisks, replace with minimal value 1
        if res[i] == '*' and res[j] == '*':
            res[i] = res[j] = '1'  # use strings for consistency
        elif res[i] == '*':
            res[i] = res[j]
        elif res[j] == '*':
            res[j] = res[i]
        elif res[i] != res[j]:
            return -1  # cannot form palindrome
    
    # If middle element is * and n is odd, set to 1
    if n % 2 == 1 and res[n // 2] == '*':
        res[n // 2] = '1'
    
    return [int(x) for x in res]

# Input Reading
n = int(input())
arr = input().split()

output = min_palindrome_array(arr)
if output == -1:
    print(-1)
else:
    print(" ".join(map(str, output)))

