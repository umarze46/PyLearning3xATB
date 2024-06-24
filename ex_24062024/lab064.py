numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def is_even(num):
    return num % 2 == 0


even_numbers = list(filter(is_even, numbers))
print(even_numbers)


def greater7(num):
    return num > 7


greater7_numbers = list(filter(greater7, numbers))
print(greater7_numbers)


def add2(num):
    return num + 2


adding2 = list(map(add2, numbers))
print(adding2)


def cube(num):
    return num ** 3


cube_numbers = list(map(cube, numbers))
print(cube_numbers)


def isodd(num):
    return num % 2 != 0


odd_numbers = list(filter(isodd, numbers))
print(odd_numbers)
