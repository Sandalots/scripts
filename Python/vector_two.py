def vector_2d(x, y):
    return (x, y)


def move_vector_2d(vector, x, y):
    return (vector[0] + x, vector[1] + y)


def amply_vector_2d(vector, factor):
    return (vector[0] * factor, vector[1] * factor)


if __name__ == "__main__":
    vec = vector_2d(3, 4)
    print(move_vector_2d(vec, 1, 2))
    print(amply_vector_2d(vec, 2))