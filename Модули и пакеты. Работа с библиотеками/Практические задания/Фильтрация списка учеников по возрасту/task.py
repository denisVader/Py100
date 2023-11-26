def calculate_average_age(student):
    return sum([student["age"] for student in student]) / len(student)


def filter_students_by_age(student, average_age):
    return [student for student in student if student["age"] < average_age]



if __name__ == '__main__':
    # Пример списка учеников
    students_list = [
        {
            "name": "Саша",
            "age": 27,
        },
        {
            "name": "Кирилл",
            "age": 52,
        },
        {
            "name": "Маша",
            "age": 14,
        },
        {
            "name": "Петя",
            "age": 36,
        },
        {
            "name": "Оля",
            "age": 43,
        },
    ]

    # Вычисление среднего возраста
    average_age = calculate_average_age(students_list)
    print("Средний возраст учеников:", average_age)

    # Фильтрация учеников по возрасту
    new_list = filter_students_by_age(students_list, average_age)
    print("Список учеников с возрастом меньше среднего: ")
    for current_student in new_list:
        print(current_student['name'])
    #print(filter_students_by_age(students_list))