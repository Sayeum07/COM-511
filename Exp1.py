'''Write a Program to demonstrate type checking of various data types 
and demonstate the use of following built in functions in python:
abs(),len(),min(),round(),isalnum(),type()'''

var_int = 42
var_float = 3.14159
var_string = "Hello, World!"
var_list = [1, 2, 3, 4, 5]
var_dict = {"name": "Alice", "age": 30}
var_bool = True


print("Variable var_int is of type:", type(var_int))
print("Variable var_float is of type:", type(var_float))
print("Variable var_string is of type:", type(var_string))
print("Variable var_list is of type:", type(var_list))
print("Variable var_dict is of type:", type(var_dict))
print("Variable var_bool is of type:", type(var_bool))


abs_value = abs(-5)
print("Absolute value of -5 is:", abs_value)


str_length = len(var_string)
list_length = len(var_list)
print("Length of var_string:", str_length)
print("Length of var_list:", list_length)

min_value = min(var_list)
print("Minimum value in var_list:", min_value)


rounded_value = round(var_float, 2)
print("Rounded value of var_float:", rounded_value)


alphanumeric_string = "Hello123"
non_alphanumeric_string = "Hello@123"
print("Is alphanumeric_string alphanumeric?", alphanumeric_string.isalnum())
print("Is non_alphanumeric_string alphanumeric?", non_alphanumeric_string.isalnum())