for i in range(100, 1000):
    sum_of_cubes = 0
    for digit in str(i):
        sum_of_cubes += int(digit) ** 3
    if sum_of_cubes == i:
        print(i)
