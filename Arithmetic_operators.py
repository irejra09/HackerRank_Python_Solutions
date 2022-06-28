# Task
# Read two integers from STDIN and print three lines where:
# 1. The first line contains the sum of the two numbers.
# 2. The second line contains the difference of the two numbers (first - second).
# 3. The third line contains the product of the two numbers.
# Input Format
# The first line contains the first integer, . The second line contains the second integer, .
# Constraints
# Output Format
# Print the three lines as explained above.
# Sample Input 0
# 3
# 2
# Sample Output 0
# 5
# 1
# 6

# Solution

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)
