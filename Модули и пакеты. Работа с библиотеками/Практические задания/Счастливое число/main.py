def is_lucky_number(num: int) -> bool:
    if num <= 0:
        raise ValueError('Число не является положительным')
    if len(str(num)) != 6:
        raise ValueError('Число не шестизначное')


    digits = [int(digit) for digit in str(num)]
    return sum(digits[:3]) ==sum(digits[3:])





    ...  # TODO проверить счастливое число или нет


print(is_lucky_number(123321))
print(is_lucky_number(111111))
print(is_lucky_number(123456))
print(is_lucky_number(456243))
