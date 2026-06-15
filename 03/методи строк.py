str_1 = "hello world   . I love you my dear so much"

print(str_1.title())
print(str_1.upper())
print(str_1.lower())
print(str_1.capitalize())
print(str_1.count('h'))
print(str_1.find('h'))
print(str_1.strip('h'))
print(str_1.strip())
print(str_1.split())
new_list = str_1.split()
print(new_list)

new_str = ' '.join(new_list)
print(new_str)