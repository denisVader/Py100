def find_common_items(last_week, current_week):
    common_ = list(set(last_week).intersection(current_week))
    common_.sort()
    return common_


last_week_items = ['книга', 'ноутбук', 'флешка', 'мышь']
current_week_items = ['ноутбук', 'флешка', 'наушники', 'монитор']

print(f"Общие товары: {find_common_items(last_week_items,current_week_items)}")  # TODO Распечатайте общие товары
