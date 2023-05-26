import re

def extract_numbers(output):
    # Extract numbers from the output using a regular expression
    number_strings = re.findall(r"[-+]?\d*\.\d+|\d+", output)

    # Convert the strings to float
    numbers = [float(num_str) for num_str in number_strings]
    return numbers

output = "@21.7@50.0@998.9\rEOF"
numbers = extract_numbers(output)
print(numbers)