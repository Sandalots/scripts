# calculate the magnitude of the given list

def mag(lst):
    return sum([x ** 2 for x in lst]) ** 0.5


print(mag([3, 4, 5]))