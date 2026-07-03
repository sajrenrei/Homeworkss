def my_decorator(func):
    def wrapper():
        print("hello before")
        func()
        print("hello after")
    return wrapper

@my_decorator             # along_function = my_decorator(along_function)
def along_function():
    print("I am along_function")


def second_function():
    a = 100
    b = 45
    print(f"Sum of  {a} and {b} is {a + b}")


along_function()

print("---------------")

second_function()