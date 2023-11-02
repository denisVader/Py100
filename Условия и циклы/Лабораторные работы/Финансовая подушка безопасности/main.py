money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
month = 0
result = money_capital + salary - spend    # После первого месяца

rate = spend + (spend * increase)
while result > 0:
    rate += rate * increase
    result = result + salary - rate
    month += 1
print(month)


print("Количество месяцев, которое можно протянуть без долгов:", month)

