speed = 4096  # скорость передачи данных в байтах/cек
time = 120  # время в минутах затраченное на скачивание игры
cost = 0.125  # стоимость за один килобайт

speed_in_kb_in_sec = 4096 / 1024
time_in_sec = 120 * 60

free_traffic = 500  # количество бесплатного трафика
file_size = speed_in_kb_in_sec * time_in_sec  # TODO размер файла
total_coast = (file_size * cost) - (500 * cost)  # TODO стоимость файла

print('Размер файла в килобайтах =', file_size)
print('За трафик придется заплатить:', total_coast)
