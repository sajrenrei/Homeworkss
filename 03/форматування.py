template = "%s is %d years old and %f meters tall"

name = "Alice"
age = 20
height = 1.75

print(template % (name, age, height))

template = "{} is {} years old and {} meters tall"
print(template.format("Alice", age, height))