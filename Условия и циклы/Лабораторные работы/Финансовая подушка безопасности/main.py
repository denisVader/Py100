money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
month = 0
# money_capital += salary - spend    # После первого месяца

# spend = spend + spend * increase
# spend = spend * (1 + increase)
# spend *= 1 + increase

# while money_capital > 0:
#     money_capital += salary - spend
#     if money_capital < 0:
#         break
#     spend *= 1 + increase
#     month += 1

while money_capital + salary - spend > 0:  # Запасов хватит
    money_capital += salary - spend  # Сколько осталось
    spend *= 1 + increase
    month += 1


print("Количество месяцев, которое можно протянуть без долгов:", month)

