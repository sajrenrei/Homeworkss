def func(a, b, **kwargs):     #**kwargs тепер робить запаковку у словник і по домовленості називають
    print(f"a: {a}")                           # kwargs
    print(f"b: {b}")
    print(f"kwargs: {kwargs}")
    for item in kwargs:
        print(f"{item}: {kwargs[item]}")
    print("-" * 20)


func(b=77, r=67, d="Hello", a=100)
func(999, b=77, r=67, d="Hello")
func(999, r=67, d="Hello", b=77)
