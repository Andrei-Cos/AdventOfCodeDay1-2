def merge(x, y):
    # Convert both integers to strings, concatenate them, and convert back to integer
    return int(str(x) + str(y))

def trebuchet(data):
    sum = 0  # Initialize sum to 0
    for i in range(len(data)):  # Loop through each string in the data list
        for char in data[i]:  # Loop through each character in the string
            if char.isdigit():  # Check if the character is a digit
                first = int(char)  # Convert the first digit found to an integer
                break  # Break the loop after finding the first digit
        for char in data[i][::-1]:  # Loop through the string in reverse
            if char.isdigit():  # Check if the character is a digit
                last = int(char)  # Convert the last digit found to an integer
                break  # Break the loop after finding the last digit
        sum += merge(first, last)  # Merge the first and last digits and add to sum

    return sum  # Return the final sum

def trebuchet2(data):
    sum = 0  # Initialize sum to 0
    for i in range(len(data)):  # Loop through each string in the data list
        data[i] = word2num(data[i])  # Convert words to numbers in the string
        for char in data[i]:  # Loop through each character in the string
            if char.isdigit():  # Check if the character is a digit
                first = int(char)  # Convert the first digit found to an integer
                break  # Break the loop after finding the first digit
        for char in data[i][::-1]:  # Loop through the string in reverse
            if char.isdigit():  # Check if the character is a digit
                last = int(char)  # Convert the last digit found to an integer
                break  # Break the loop after finding the last digit
        sum += merge(first, last)  # Merge the first and last digits and add to sum

    return sum  # Return the final sum

def word2num(mot):
    # Dictionary mapping words to a specific string format
    dico = {
        'one': 'one1one',
        'two': 'two2two',
        'three': 'three3three',
        'four': 'four4four',
        'five': 'five5five',
        'six': 'six6six',
        'eight': 'eight8eight',
        'nine': 'nine9nine'
    }
    for word, number in dico.items():  # Loop through the dictionary
        mot = mot.replace(word, str(number))  # Replace words with their number format
    digits = [char for char in mot if char.isdigit()]  # Extract all digits from the string
    digits = (''.join(digits))  # Join all digits into a single string
    return digits  # Return the string of digits

if __name__ == "__main__":
    f = open("input_day_1.txt", "r")  # Open the input file for reading
    data = f.readlines()  # Read all lines from the file
    f.close()  # Close the file
    for i in range(len(data)):  # Loop through each line in the data
        data[i] = data[i].rstrip()  # Remove trailing newline character from each line

    print(trebuchet(data))  # Print the result of the trebuchet function
    print(trebuchet2(data))  # Print the result of the trebuchet2 function
