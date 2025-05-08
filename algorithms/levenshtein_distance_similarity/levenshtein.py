import numpy as np


def minimum(a, b, c):
    if a < b and a < c:
        return a
    if b < c and b < a:
        return b
    if c < a and c < b:
        return c


def max(a, b):
    if a > b:
        return a
    else:
        return b


def normalize(x, size):
    if len(x) < size:
        difference = size - len(x)
        for i in range(difference):
            x = x + ' '
    return x


def levenshtein(a, b):
    a_len = len(a)
    b_len = len(b)
    k = np.zeros((a_len + 1, b_len + 1), dtype=int)
    for i in range(a_len):
        k[i][0] = i
    for i in range(b_len):
        k[0][i] = i
    delete = 0
    add = 0
    change = 0

    for i in range(1, a_len + 1):
        for j in range(1, b_len + 1):
            if a[i - 1] == b[j - 1]:
                k[i][j] = k[i - 1][j - 1]
            else:
                delete = k[i - 1][j] + 1
                add = k[i][j - 1] + 1
                change = k[i - 1][j - 1] + 1
                k[i][j] = min(delete, add, change)
    return k[a_len][b_len]
