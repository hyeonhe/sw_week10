def to_uppercase(input_string):
    return input_string.upper()

# 예제 사용
original_string = "hello, world!"
uppercase_string = to_uppercase(original_string)
print(uppercase_string)

def add_numbers(num1, num2):
    return num1 + num2

# 예제 사용
result = add_numbers(3, 5)
print(result)

def is_even(number):
    return number % 2 == 0

# 예제 사용
number_to_check = 4
if is_even(number_to_check):
    print(f"{number_to_check} is even.")
else:
    print(f"{number_to_check} is odd.")

def concatenate_strings(str1, str2):
    return str1 + str2

# 예제 사용
string1 = "Hello, "
string2 = "world!"
concatenated_string = concatenate_strings(string1, string2)
print(concatenated_string)

def count_elements(input_list):
    return len(input_list)

# 예제 사용
my_list = [1, 2, 3, 4, 5]
element_count = count_elements(my_list)
print(element_count)