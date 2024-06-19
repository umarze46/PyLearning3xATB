numbers = [1, 2, 3]


def do_something(umar_list):
    umar_list.append(100)
    umar_list[1] = 20

    return numbers

numbers.append(300)
f = do_something(numbers)
print(f)
