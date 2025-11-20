# The program must accept a string 
# S
# S containing alphabet-integer pairs as the input. For each alphabet-integer pair (CH-X), the program must form a square matrix of size 
# X
# ×
# X
# X×X with the alphabet CH. Then the program must print those matrices horizontally as shown in the Example Input/Output section. The empty spaces must be printed as asterisks.

# Boundary Condition(s):

# 2
# ≤
# 2≤ Length of 
# S
# ≤
# 100
# S≤100

# 1
# ≤
# X
# ≤
# 15
# 1≤X≤15

# Input Format:
# The first line contains S.

# Output Format:
# The lines contain the matrices horizontally as shown in the Example Input/Output section.

# Example Input/Output 1:

# Input:

# text
# a3b4c5d2
# Output:

# text
# a a a b b b b c c c c c d d
# a a a b b b b c c c c c d d
# a a a b b b b c c c c c * *
# * * * b b b b c c c c c * *
# * * * * * * c c c c c * *
# * * * * * * c c c c c * *
# Explanation:
# Here the given string is a3b4c5d2.

# For the 1st pair (a, 3) the 3x3 matrix is printed.

# For the 2nd pair (b, 4) the 4x4 matrix is printed.

# For the 3rd pair (c, 5) the 5x5 matrix is printed.

# For the 4th pair (d, 2) the 2x2 matrix is printed.

ss = input().strip()
i = 0
list_a = []

while i < len(ss):
    ch = ss[i]
    i += 1
    num = ''
    while i < len(ss) and ss[i].isdigit():
        num += ss[i]
        i += 1
    list_a.append((ch, int(num)))
m = max(n for _, n in list_a)
for n in range(m):
    parts = []
    for ch, ln in list_a:
        if n < ln:
            parts.append(ch * 1)
        else:
            parts.append('*' * 1)
    print(''.join(parts))

