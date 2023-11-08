list_ = [3, 4, 8, 9, 6, 6, 2, 4, 3, 3, 1]

# TODO завести отдельные счетчики для четных и нечетных чисел
even = 0
not_even =0

# TODO с помощью одного цикла перебрать все числа и посчитать количество четных и нечетных
for i in list_:
    if i % 2 == 0:
        even += 1
    else:
        not_even += 1


if even > not_even:
    print("Четных чисел больше")
elif not_even > even:
    print("Нечетных чисел больше")
else:
    print("Четных и нечетных чисел одинаковое количество")

#print(even)
#print(not_even)


