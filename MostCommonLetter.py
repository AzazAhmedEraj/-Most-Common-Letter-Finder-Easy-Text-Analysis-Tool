# Function to find the most common letter in a string
def find_most_common_letter(text):
    # Remove non-alphabetic characters and convert to lowercase
    filtered_text = ''.join([char.lower() for char in text if char.isalpha()])
    
    # Create a dictionary to count the occurrences of each letter
    letter_counts = {}
    
    for letter in filtered_text:
        letter_counts[letter] = letter_counts.get(letter, 0) + 1
    
    # Find the most common letter
    most_common_letter = max(letter_counts, key=letter_counts.get)
    
    return most_common_letter, letter_counts[most_common_letter]

# Taking user input
text = input("Enter the text: ")

# Find and display the most common letter and its count using a simpler print
letter, count = find_most_common_letter(text)
print("The most common letter is", letter.upper(), "with", count, "occurrences.")
