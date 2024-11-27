# Write a recursive function to calculate the sum of first n natural numbers.
# 5 + 4 + 3 + 2 +1
def sum(n):
    if n==0:
        return 0
    else:
        return n + sum(n-1)
n = 5
print(sum(n))