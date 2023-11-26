import json


FILENAME = "input.json"


def task() -> dict:
    with open(FILENAME) as f:
        json_data = json.load(f) # TODO считать содержимое JSON файла

    return max(json_data, key=lambda item: item["score"])  # TODO найти максимальный элемент по ключу score


if __name__ == '__main__':
    print(task())
