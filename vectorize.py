import numpy as np
import random


def normalize_number(number, min, max):
    return (number-min)/(max-min)


def init_list(index, size):
    # out = [0]*size
    # out[index] = 1
    # return out
    return index


def normalize_attributes(age, dept, dist, edu_lvl, edu_field, env, sat, married, income, prev, balance, years):
    attributes = [0] * 12
    attributes[0] = normalize_number(age, 18, 60)
    attributes[1] = init_list(dept, 3)
    attributes[2] = normalize_number(dist, 1, 29)
    attributes[3] = init_list(edu_lvl - 1, 5)
    attributes[4] = init_list(edu_field, 6)
    attributes[5] = init_list(env - 1, 4)
    attributes[6] = init_list(sat - 1, 4)
    attributes[7] = init_list(married, 3)
    attributes[8] = normalize_number(income, 1009, 20000)
    attributes[9] = normalize_number(prev, 0, 9)
    attributes[10] = init_list(balance - 1, 4)
    attributes[11] = normalize_number(years, 0, 40)
    return attributes


def vectorize_data(data, normalize=True):
    x, y = [], [0] * len(data)
    for i, row in enumerate(data):
        y[i] = row[1]
        x += [normalize_attributes(row[0], *row[2:])] if normalize else [[row[0]] + row[2:]]
    return x, y


def randomize(x, y):
    print('randomizing')
    rand_order = list(zip(x, y))
    random.shuffle(rand_order)
    x_out, y_out = [], []
    for features, label in rand_order:
        x_out += [features]
        y_out += [label]
    return x_out, y_out
