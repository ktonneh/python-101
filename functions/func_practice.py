def my_print_function():
    print('This is ')
    print('a function')

def minimum(first,second):
    """
    This function returns 
    the smallest of the 2 numbers 
    that are provided
    """
    if(first < second):
        return first
    else:
        return second

def area_circle(radius):
    return 3.14 * (radius ** 2)    




# my_print_function()

print(minimum.__doc__)
print(f"Min between 2 & 5 is: {minimum(2,2)}")
print(f"The area of the circle is {area_circle(10)}")


numlist = [10,20,30,40]
print(numlist)

def multiply_by_ten(numlist):
    numlist[0] *= 10
    numlist[1] *= 10
    numlist[2] *= 10
    numlist[3] *= 10

multiply_by_ten(numlist)
print(numlist)

print('----------------------------------')
print('----------------------------------')


