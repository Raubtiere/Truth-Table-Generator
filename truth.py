from itertools import product


def retrieve_letters():
    logical_statements = ['not', 'or', 'and']
    truth_inp = input("Formula: ")
    only_alpha = ""
    only_alpha += "".join(char for char in truth_inp if 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122)
    for logical in logical_statements:
        only_alpha = only_alpha.replace(logical, " ")
    return ''.join(dict.fromkeys(only_alpha)).replace(" ", "")


def truth():
    var_count = [letter for letter in retrieve_letters()]
    return list(product([True, False], repeat=len(var_count)))


if __name__ == "__main__":
    print(truth())
