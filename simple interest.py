# simple_interest.py

# Function to sum two numbers
def sum_of_two_numbers(num1, num2):
    return num1 + num2

# Main code
if __name__ == "__main__":
    # Input from the user
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    
    # Calculate the sum
    result = sum_of_two_numbers(number1, number2)
    
    # Display the result
    print(f"The sum of {number1} and {number2} is: {result}")