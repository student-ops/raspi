import re
numbers = "@7.0 @-8.0 @9.0 "
number_strings = re.findall(r"[-+]?\d*\.?\d+", numbers)
# number_strings = re.findall(r"\d+", numbers)
print(number_strings)
print(type(number_strings))