def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def divide(n1,n2):
    return n1 / n2

def multiply(n1,n2):
    return n1 * n2

def calculator(operation,n1,n2):
    return operation(n1,n2)

print(calculator(add,10,20))  

result = calculator(multiply,10,20)

print(result)
# with lambda

res = calculator(lambda n1, n2: n1 * n2,10,20)

print(res)