def example_function(a, b, c):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"c: {c}")
    print("-" * 20)

my_dict = {"a": 1, "b": 2, "c": 3}
example_function(**my_dict)       #example_function(a=1, b=2, c=3)