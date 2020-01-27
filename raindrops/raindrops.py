word = {3: 'Pling',
        5: 'Plang',
        7: 'Plong'}


def convert(number):

    result = ''

    for key, value in word.items():
        if number % key is 0:
            result += value

    return str(number) if not result else result
