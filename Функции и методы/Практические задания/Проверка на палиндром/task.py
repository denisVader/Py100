def is_palindrome(str_polindrom):
    str_ = ''.join(str_polindrom.lower().split())
    return str_ == str_[::-1]


