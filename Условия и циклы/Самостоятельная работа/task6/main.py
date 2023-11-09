list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_num_index = 0
max_num = list_numbers[max_num_index]
for i, num in enumerate(list_numbers):
    if num >= max_num:
        max_num = num
        max_num_index = i
# print(max_num, max_num_index)
# print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]

# a = list_numbers[-1]
# b = list_numbers[max_num_index]
list_numbers[-1], list_numbers[max_num_index] = list_numbers[max_num_index], list_numbers[-1]
print(list_numbers)

# print(list_numbers[-1])
# print(list_numbers[max_num_index])