# Function to print ASCII values of alphabets
def print_ascii_values():
    # Loop through all uppercase and lowercase alphabets
    for char in range(65, 91):  # Uppercase A-Z
        print(f"'{chr(char)}' : {char}")
    
    for char in range(97, 123):  # Lowercase a-z
        print(f"'{chr(char)}' : {char}")

# Call the function
print_ascii_values()
