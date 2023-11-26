def sort_participants(partticipants_list):
    return participants_list


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

    participants_list = sorted(participants_list,key=lambda a: a["name"])
    print(sort_participants(participants_list))
