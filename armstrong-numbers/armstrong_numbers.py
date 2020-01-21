from math import pow


def is_armstrong_number(number):
    number_str = str(number)
    power = len(number_str)
    result = 0
    for char in number_str:
        result += pow(int(char), power)

    if result == number:
        return True
    else:
        return False
