year = 2012

if 4*(year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):

    print(year, "является високосным годом.")
else:
    print(year, "не является високосным годом.")
