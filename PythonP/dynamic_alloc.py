import random

size = random.randint(1, 100)
buffer = []


def create_buffer():
    for x in range(size):
        buffer.append([])
        for y in range(size):
            buffer[x].append(0)

    return buffer

buffer = create_buffer()

print(buffer)