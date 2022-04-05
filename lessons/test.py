class Point:
    x: int
    y: int

    def __str__(self) -> str:
        return "hello world"

    def __repr__(self) -> str:
        return "Point(\"hello world\")"


test: Point = Point()
print(repr(test))