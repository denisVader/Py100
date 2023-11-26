def get_shortest_word(words: list[str])-> str:
    return min(words, key=len)




if __name__ == "__main__":
    words_list = ["apple", "banana", "orange", "grapefruit", "kiwi"]
    shortest_word = get_shortest_word(words_list)
    print(shortest_word)  # kiwi
