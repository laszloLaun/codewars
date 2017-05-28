from itertools import cycle


def coordinate_generator(length):
    coord = 11
    yield coord
    modifiers = cycle([1, 10, -1, -10])
    modifier = 1
    modifier_controller = length - 1
    range_max = length * length
    multipliers = [3, 3, 3]
    for i in range(0, length - 1):
        multipliers.append(2)
    print(multipliers)

    for i in range(1, range_max):
        print("i:", i, "modifier_controller:", modifier_controller)
        print(i % modifier_controller != 0)
        if i % (modifier_controller) != 0:
            modifier = next(modifiers)
        coord += modifier
        print("coord:", coord)
        yield coord

        print("length:", length)


def snail(array):
    length = len(array)
    coord_gen = coordinate_generator(length)
    solution = []
    square = length * length
    for i in range(square):
        coord = next(coord_gen)
        solution.append(array[int(str(coord)[0]) - 1][int(str(coord)[1]) - 1])

    print(solution)
    return solution


snail([[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]])
