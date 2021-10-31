import functools


def matrixify(func):
    """transfer scalar function to matrix function, result is a function"""

    def wrapper(matrix1, matrix2=None):
        if matrix2 is None:
            return [[func(item) for item in row] for row in matrix1]
        else:
            return [[func(matrix1[row][col], matrix2[row][col])
                     for col in range(len(matrix1[0]))]
                    for row in range(len(matrix1))]

    return wrapper


def reduce(func, axis=0):
    """change a function to a reduce action"""

    def wrapper(matrix):
        if axis == 0:
            return list(map(lambda seq: functools.reduce(func, seq[1:], seq[0]), matrix))
        else:  # axis == 1
            return [functools.reduce(func, [row[i] for row in matrix[1:]], matrix[0][i]) for i in range(len(matrix[0]))]

    return wrapper


def product(func, vector1, vector2):
    """out product two vectors to matrix"""
    return [[func(item1, item2) for item2 in vector2] for item1 in vector1]


def solve(matrix):
    return matrixify(int.__mul__)(
        matrix,
        matrixify(lambda x: x > 0)(
            product(
                min,
                reduce(min, 0)(matrix),
                reduce(min, 1)(matrix))))


if __name__ == '__main__':
    print(solve([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
    print(solve([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]))

    # print(matrixify(int.__add__)(matrix, matrix))
    # print(matrixify(lambda x: x > 0)(matrix))

    # print(reduce(min, 0)(matrix))
    # print(reduce(min, 1)(matrix))

    # print(product(int.__add__, [100, 200], [1, 2, 3]))
