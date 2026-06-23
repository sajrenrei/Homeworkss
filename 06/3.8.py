def func(a,b,c=99, d=None):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"c: {c}")
    print(f"d: {d}")

a = 10
b = 56
c = 0
func(c, a, b)
print("-" * 20)
func(c, a)
func(c, a,{"5": 5, "7": 7, "6": 6})
     