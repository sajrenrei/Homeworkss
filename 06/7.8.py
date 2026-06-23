def func(*args, **kwargs):    #Ця ф-я може приймати все що завгодно
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")
    print("-" * 20)


func(b=77, r=67, d="Hello", a=100)
func(999, b=77, r=67, d="Hello")
func(999, r=67, d="Hello", b=77)
func(999, 56, 77 ,67, r=67, d="Hello", b=77)
func(999, 56, 77 ,67)
func(r=67, d="Hello", b=77)
func()
