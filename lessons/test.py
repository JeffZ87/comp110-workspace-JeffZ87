x: int = 2


def hello() -> None:
    # x: int = 3
    global x
    x = 1
    print(x)


hello()
print(x)