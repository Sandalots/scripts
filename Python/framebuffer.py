import time

def frame_buffer():
    frame_buffer = [[]]
    for x in range(640):
        frame_buffer.append([])
        for y in range(480):
            frame_buffer[x].append(0)

    return frame_buffer


def update_frame_buffer(frame_buffer, x, y, value):
    frame_buffer[x][y] = value
    return frame_buffer


# update every even pixel to 1 if set to 0 and 0 if set to 1
def update_frame_buffer_even(frame_buffer):
    # every even pixel
    for x in range(0, 640, 2):
        for y in range(0, 480, 2):
            if frame_buffer[x][y] == 0:
                frame_buffer[x][y] = 1
            else:
                frame_buffer[x][y] = 0

    return frame_buffer


# print the frame buffer without the '[' and ']' and ',' characters
def print_frame_buffer(frame_buffer):
    for x in range(640):
        for y in range(480):
            print(frame_buffer[x][y], end="")
        print()

if __name__ == "__main__":
   #print_frame_buffer(frame_buffer())
   #update_frame_buffer(frame_buffer(), 320, 240, 255)
    fb = frame_buffer()
    while True:
        print(update_frame_buffer_even(fb))
        # wait for 5 seconds
        time.sleep(5)
