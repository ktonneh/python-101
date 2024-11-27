# This program outputs remainder of 2 numbers divided

def calculate(num1,num2):
    return num1%num2;

def average(num1,num2):
    return (num1+num2) / 2;


def main():
    num1 = int(input('Enter Num1 \n'))
    num2 = int(input('Enter Num2 \n'))

    print('Remainder of ',num1,' / ',num2,'=',calculate(num1,num2))
    print('Average of ',num1,' / ',num2,'=',average(num1,num2))

main()