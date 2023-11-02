salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
money_capital = 0
money_capital = spend - salary   # Требуемая сумма в 1 месяце
rate = spend + (spend * increase)    # Инфляция за месяц

for i in range(9):    # -1 т.к 1 месяц мы посчитали без повышений
    rate += rate * increase    # Увличение инфляции ежемесячно
    money_capital = money_capital + salary - rate
print(rate)
print(money_capital)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", f"{money_capital:.2f}")



# 18783

