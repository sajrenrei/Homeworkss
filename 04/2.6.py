my_list = [1,2,3,4,5,6,7,8,9,10]
print(my_list)
my_list_2 = list((1,2,3,4,5,6,7,8,9,10))
print(my_list_2)

my_tuple = (1,2,3,4,5,6,7,8,9,10)
print(my_tuple)
my_tuple_2 = tuple((1,2,3,4,5,6,7,8,9,10))
print(my_tuple_2)

print(id(my_list))
print(id(my_tuple))
print(id(my_list_2))
print(id(my_tuple_2))

input_data = input("Enter your data with comma separated values: ").split(", ")
print(input_data)

input_data_2 = tuple(input("Enter your data with comma separated values: ").split(", "))
print(input_data_2)

input_data_3 = [int(item) for item in input("Enter your data with comma separated values: ").split(",")]
print(input_data_3)

input_data_4 = tuple(int(item) for item in input("Enter your data with comma separated values: ").split(","))
print(input_data_4)