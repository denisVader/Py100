def get_list_number_divisors(number):
    list_divisors = []
    for divisors in range(1, number + 1):
        if number % divisors == 0:
            list_divisors.append(divisors)
    return list_divisors
print(get_list_number_divisors(23))
print(get_list_number_divisors(2 ** 16))