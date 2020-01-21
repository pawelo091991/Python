def convert(number):
    word = {3: 'Pling',
            5: 'Plang',
            7: 'Plong'}

    result = ''

    for key in word:
        if number % key is 0:
            result += word[key]

    if result is '':
        return str(number)
    else:
        return result

