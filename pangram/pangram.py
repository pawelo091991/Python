import string


def is_pangram(sentence):
    alphabet = string.ascii_lowercase
    sentence = sentence.lower()
    for char in alphabet:
        if char not in sentence:
            return False
    return True
