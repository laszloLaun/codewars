def faulty_odometer(n):
    count = 0
    for i in range(n + 1):
        if "4" in str(i):
            count += 1

    print(n - count)
    return n - count


faulty_odometer(11111)
