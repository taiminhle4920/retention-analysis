import numpy as np


def write_to_file(name, x, y):
    lines = []
    for x_row, y_row in zip(x, y):
        lines += [str(x_row) + '|' + str(y_row) + '\n']
    with open(name, 'w') as file:
        file.writelines(lines)


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def extract_type(input_string):
    if input_string == 'None':
        return None
    # if input_string.replace('-', '').isdigit():
    #     return int(input_string)
    if isfloat(input_string):
        return float(input_string)
    if input_string.isbool():
        return bool(input_string)
    return input_string


def parse_tensor_helper(input_list):
    out = []
    i = 0
    while i < len(input_list):
        if input_list[i][0] == '[':
            parsed, length = parse_tensor_helper([input_list[i][1:]] + input_list[i + 1:])
            out += [parsed]
            i += length
        elif input_list[i][-1] == ']':
            out += [extract_type(input_list[i][:-1])]
            return out, i
        else:
            out += [extract_type(input_list[i])]
        i += 1
    return None, 0


def parse_tensor(input_string):
    input_list = input_string.replace(', ', ',')[1:].split(',')
    return parse_tensor_helper(input_list)[0]


def read_data_file(name):
    with open(name, 'r') as file:
        lines = file.readlines()
    x_out, y_out = [], []
    for line in lines:
        x, y = line.split('|')
        x_out += [parse_tensor(x)]
        y_out += [int(y[0])]
    return x_out, y_out
