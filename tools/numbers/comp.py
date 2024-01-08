print ("SumOfDigits function:")
# Function to calculate the sum of digits in a given number
def sumOfDigits(number):
    # Convert the number to a string to iterate through its digits
    num_str = str(number)
    
    # Initialize a variable to store the sum of digits
    digit_sum = 0
    
    # Iterate through each digit in the string and add it to the sum
    for digit in num_str:
        digit_sum += int(digit)
    
    # Return the calculated sum of digits
    return digit_sum

# Example usage:
selected_number = 222
result = sumOfDigits(selected_number)

# Print the result along with a descriptive message
print("The summary of", selected_number, "is", result)

print ("-------------------------------")

print ("ispal function:")
# Define the function to check if a number is a palindrome
def ispal(num):
    # Convert the number to a string for easier comparison
    num_str = str(num)
    
    # Check if the string is equal to its reverse
    return num_str == num_str[::-1]

# Example usage:

# Palindrome number
palindrome_number = 121

# Non-palindrome number
non_palindrome_number = 456

# Check if the first number is a palindrome
result_palindrome = ispal(palindrome_number)
if result_palindrome:
    print(f"The number {palindrome_number} is a palindrome.")
else:
    print(f"The number {palindrome_number} is not a palindrome.")

# Check if the second number is a palindrome
result_non_palindrome = ispal(non_palindrome_number)
if result_non_palindrome:
    print(f"The number {non_palindrome_number} is a palindrome.")
else:
    print(f"The number {non_palindrome_number} is not a palindrome.")

    print ("-------------------------------")