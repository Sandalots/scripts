import random

buffer = []

def create_buffer():
    for x in range(8):
        buffer.append([])
        for y in range(8):
            buffer[x].append(0)

    return buffer


buffer = create_buffer()


# make a 50/50 chance of setting a pixel to 1
def randomize_buffer():
    for x in range(len(buffer)):
        for y in range(len(buffer[x])):
            if random.random() > 0.5:
                buffer[x][y] = 1

    return buffer


buffer = randomize_buffer()

print(buffer)


def calculate_binary_value(buffer):
   for x in range(len(buffer)):
       binary_value = 0
       for y in range(len(buffer[x])):
           binary_value += buffer[x][y] * (2 ** y)

       print(binary_value)

    

calculate_binary_value(buffer)