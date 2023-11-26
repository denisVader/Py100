import json


FILENAME = "input.json"


def task() -> int:
    with open(FILENAME) as f:
        json_data = json.load(f)  # TODO Десериализуйте содержимое JSON файла

    list_values = [item["contains_improvement_appeals"] for item in json_data]
    return sum(list_values)  # TODO Просуммируйте все значения по ключу contains_improvement_appeals


if __name__ == '__main__':
    print(task())
