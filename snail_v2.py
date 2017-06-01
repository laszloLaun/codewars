from itertools import cycle


def snail(array):

    if array == [[]]:
        return []

    elif len(array) == 1:
        return [1]

    elif len(array) == 2:
        return [1, 2, 4, 3]

    solution = []
    length = len(array) - 1
    coord = 11
    solution.append(array[int(str(coord)[0]) - 1][int(str(coord)[1]) - 1])
    modifiers = cycle([1, 10, -1, -10])
    modifier = next(modifiers)

    for i in range(3):
        for i in range(length):
            coord += modifier
            solution.append(array[int(str(coord)[0]) - 1]
                            [int(str(coord)[1]) - 1])
        modifier = next(modifiers)
    length -= 1

    while length > 0:
        for i in range(2):
            for i in range(length):
                coord += modifier
                solution.append(array[int(str(coord)[0]) - 1]
                                [int(str(coord)[1]) - 1])
            modifier = next(modifiers)
        length -= 1

    return solution


'''snail([[1,2,3],
       [4,5,6],
       [7,8,9]])'''

'''snail([[1,2,3,4,5],
       [6,7,8,9,10],
       [11,12,13,14,15],
       [16,17,18,19,20],
       [21,22,23,24,25]])'''

'''snail([[1,2,3,4,5,6],
       [7,8,9,10,11,12],
       [13,14,15,16,17,18],
       [19,20,21,22,23,24],
       [25,26,27,28,29,30],
       [31,32,33,34,35,36]])'''
