# Вам дана лямбда функция foo, перепишите ее на обычную функцию.


foo = lambda **kwargs: {v: k for k, v in kwargs.items()}

if __name__ == "__main__":
    print(foo(a=1, b=2))
