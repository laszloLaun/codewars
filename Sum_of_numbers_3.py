def get_sum(a, b):
    print(a, b)
    if b >= 0:
        if b > a:
            print(sum(list(range(a, b + 1))))
            return sum(list(range(a, b + 1)))
        elif a > b:
            print(sum(list(range(a, b - 1, -1))))
            return sum(list(range(a, b - 1, -1)))
        elif a == b:
            print(a)
            return a
    elif b < 0:
        if b < a:
            print(sum(list(range(a, b - 1, -1))))
            return sum(list(range(a, b - 1, -1)))
        elif a < b:
            print(sum(list(range(a, b + 1,))))
            return sum(list(range(a, b + 1)))
        elif a == b:
            print(a)
            return a

get_sum(-5, -1)
