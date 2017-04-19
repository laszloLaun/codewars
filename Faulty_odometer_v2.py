def faulty_odometer(n):
    n = str(n)
    ind = len(n) - 1
    total = 0
    power_of_ten = 0
    while ind >= 0:
        if int(n[ind]) >= 4:
            total += int(n[ind]) * (10**power_of_ten)
        ind -= 1
        power_of_ten += 1
    print(int(n) - total)


faulty_odometer(5555)
