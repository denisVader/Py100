def get_oldest_participant():
    return oldest_participant


if __name__ == "__main__":
    participants_list = [
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

    oldest_participant = max(participants_list, key=lambda a: a["age"]) # TODO Найдите самого старшего участника
    print(get_oldest_participant())
