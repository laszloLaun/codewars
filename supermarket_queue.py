def queue_time(customers, n):
    l = [0] * n
    for i in customers:
        l[l.index(min(l))] += i
        print(l)
    print(max(l))
    return max(l)

queue_time([22, 41, 44, 29, 17, 21, 5, 3], 3)
