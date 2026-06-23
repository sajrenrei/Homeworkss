def func(*args):           # * - це оператор запаковки. Пакує все в кортежі або списки
  #  print(f"args: {args}")     # args - це домовленість між програмістами називати так змінну. Може бути
    for item in args:           #будь яке значення змінної, наприклад "a"
        print(item)
    print("-" * 20)

a = 10
b = 56
c = 0
func(c, a, 556)
func(c, a)
func(c)
func(c, a, 556, "ewter", 767, -100, 0, "dsgdf", [1, 33, {3: "Hell0"}, 89])
func()