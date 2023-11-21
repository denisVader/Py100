def get_sentences_list(str_):
    new = []
    for sentence in str_.split("."):
        if sentence:
            new.append(sentence.strip())
    return new



print(get_sentences_list("Здесь много разных слов. Возможно и много повторений..."))
