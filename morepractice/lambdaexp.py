triple = lambda num: num * 3

print(triple(10))

print_triple = lambda num: print(num*3)

print_triple(12)

hardcoded_triple = lambda: 18 * 3

print(hardcoded_triple())

# conditional with lambda

my_func =  lambda num: "High" if num > 50 else "Low"

print(my_func(10))