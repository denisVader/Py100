def remove_whitespace(str_with_space):
    res = str_with_space.split(" ")

    #return res
    new_text = []
    for text in res:
        if text:
            new_text.append(text)
    return " ".join(new_text)

    #res = " ".join(str_with_space.split())
    #print(res)
    #return res


str_with_space = """123.    test bks
print   test11"""  # исходная строка
print(remove_whitespace(str_with_space))
