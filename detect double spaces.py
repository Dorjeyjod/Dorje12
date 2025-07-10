def detect_double_spaces(input_string):
    if '  ' in input_string:
        return True
    return False

# Example usage
test_string = "This is  a test string with  double spaces."
result = detect_double_spaces(test_string)
print("Double spaces detected:", result)