letter = "Dear students,\n\tThis python course is going well.\n\tThanks!"
print(letter)

def detect_double_spaces(letter):
    if '  ' in letter:
        return True
    return False

#Example usage
test_string = "This is  a test string with  double spaces."

#Detect double spaces
result = detect_double_spaces(test_string)
print("Double spaces detected:", result)

#Replace double spaces with single spaces
fixed_string = test_string.replace('  ', ' ')
print("Fixed string:", fixed_string)