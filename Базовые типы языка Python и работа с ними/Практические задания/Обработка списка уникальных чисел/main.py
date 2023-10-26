list_ = [8, 9, -5, -3, 1, -10, 8, -10, -5, 0, 5, -4, 0, 10, -8, 1, 6, -6, 6, -9]

# TODO найти сумму, количество и среднее арифметическое уникальных чисел
numbers = set(list_)
sum_of_numbers = sum(numbers)
count_of_numbers = len(numbers)
average = sum_of_numbers / count_of_numbers
a = 'Сумма уникальных чисел:'
b = 'Количество уникальных чисел:'
c = 'Среднее арифметическое уникальных чисел:'
# describe = {a:sum_of_numbers,b:count_of_numbers,c: float(f'{average:.5f}')}
describe = {a: sum_of_numbers, b: count_of_numbers, c: round(average, 5)}
print(describe)
