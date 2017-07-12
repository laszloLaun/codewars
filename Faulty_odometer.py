def faulty_odometer(n):
    start = 0
    count = 0
    start_local = 0
    count_local = 0
    if n >= 1000:    # calculations
        n = str(n)
        length = len(n)

        for num in range(length - 2):
            if int(n[num]) >= 1 and int(n[num]) <= 3:
                start_local += 10**(length - 1) * int(n[num])         # brute force start
                count_local += start_local - 9**(length - 1) * int(n[num])  # total occurence of 4's in n
                start += start_local
                count += count_local
                start_local = 0
                count_local = 0
            elif int(n[num]) >= 5 and int(n[num]) <= 9:
                start_local += 10**(length - 1) * (int(n[num]))
                count_local += start_local - 9**(length - 1) * (int(n[num]) - 1)
                start += start_local
                count += count_local
                start_local = 0
                count_local = 0
            length -= 1
    n = int(n)
    for i in range(start, n + 1):  # brute force
        if "4" in str(i):
            count += 1
    print(n - count)
    return n - count
faulty_odometer(111111)
