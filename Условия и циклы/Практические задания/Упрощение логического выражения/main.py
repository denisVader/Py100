is_active = True  # Статус активен пользователь или нет
is_blocked = False  # # Статус заблокирован пользователь или нет

if is_active and not is_blocked:
    print("Пользователь прошел проверку")
else:
    print("Пользователь не прошел проверку")
