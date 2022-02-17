def test(i: list[int]) -> None:
    i.append(i[0])


def test_str(i: str) -> None:
    i = ""


a: list[int] = list([10, 20, 30])
test(a)
print(a)

string: str = "hello"
test_str(string)
print(string)