# Нужно реализовать функцию convert,
# которая должна преобразовывать строку input_str
# в массив аски-кодов (https://ru.wikipedia.org/wiki/ASCII).
# ASCII -  таблица, в которой некоторым распространённым
# печатным и непечатным символам сопоставлены числовые коды.
# Для получения кода ASCII нужно воспользоваться функцией ord.
# https://docs.python.org/3/library/functions.html#ord


input_str = "hello my friend"


def convert(input_str):
    return (ord(item) for item in input_str)


if __name__ == "__main__":
    print([x for x in convert(input_str)])
