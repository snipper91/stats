def data_number_check(data):

    is_digit = True
    for digit in data:
        if digit.isdigit() or digit == ',':
            continue
        else:
            is_digit = False
    return is_digit