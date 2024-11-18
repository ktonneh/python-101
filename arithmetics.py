def calculate_area(length,width):
    return length * width

def calc_circumference(radius):
    PI = 3.142
    return 2*PI*radius


def main():
    side_a = int(input('Enter length\n'))
    side_b = int(input('Enter Width\n'))

    area = calculate_area(side_a,side_b)
    print('Area:',area)


main()