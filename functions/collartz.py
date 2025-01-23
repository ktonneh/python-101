'''
The Collatz conjecture is a mathematical sequence defined as follows: Start with any positive integer n. Then, each term is obtained from the previous term as follows:

If the previous term is even, the next term is one half of the previous term.

If the previous term is odd, the next term is 3 times the previous term plus 1.

The conjecture states that no matter what number you start with, by repeating the above mentioned steps, you will always reach the number 1. Let's test this conjecture programmatically.
Takes a positive integer n as input.

Generates and returns the Collatz sequence starting from n.

'''


def collatz_sequence(n):
    if(n==1):
        return 1
    if((n-1) % 2 ==0):
        return collatz_sequence((n-1)/2)
    else:
        return collatz_sequence(((n-1)*3)+1)
    

print(collatz_sequence(3))   

