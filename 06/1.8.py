name = "Yevhen"

# def func1():                  #Це неявно прокинута функція. Так краще не робити. Можна легко заплутатись
#     global name
#     name = "Bob"
#     print("Hello," + name + "!")


# def func2():                  #Це неявно прокинута функція. Так краще не робити. Можна легко заплутатись
#     print("Ciao," + name + "!")


def func1():
    name = "Bob"
    print("Hello," + name + "!")
    return name

def func2(name):
    print("Ciao," + name + "!")


print("Hello," + name + "!")
name = func1()
func2(name)


