"""An example of for in syntax."""

names: list[str] = ["Jeff", "Kris", "Zhuo", "Jordan"]

# Example of iterating through name using while loop
print("while output: \n")
i: int = 0
while i < len(names):
    name: str = names[i]
    print(name)
    i += 1

# The following for...in loop is the same as above
print("for...in output: \n")
for name in names:
    print(name)