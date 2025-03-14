# Function to return first_name
def first_name():
    return "Joy"

# Function to return the last_name
def last_name():
    return "Airhunmwunde"

# Function to concatenate the first and last name
def full_name():
    first = first_name()
    last = last_name()
    return f"My full name is {first} {last}."

# Example usage
print(full_name())


#list of attributes
attributes = ["first name", "last_name", "date of birth"]

#Transform the attributes by replacing spaces with underscores
transformed_attributes = [attr.replace(" ", "_") for attr in attributes]

# Print the result
print(transformed_attributes)


#list of names
names = ["Mayowa", "chizoba", "Chigozie"]

# Make a new empty list for the final names
final_names = []

# check through the names
for name in names:
    # Check if first letter is a capital letter
    if name[0] == name[0].upper():
        # Check if last letter is 'a'
        if name[-1] == 'a':
            final_names.append(name)  
        else:
            # Make new name by taking all letters except last one and adding 'a'
            new_names = name[0:-1] + 'a'
            final_names.append(new_names)

# Print result
print(final_names)


# Write a function to validate name checks for the marketing team
def check_names(customer_list):
    # Look through the 
    for name in customer_list:
        # Look at each letter in the names
        for letter in name:
            # If a number is found, show error and stop
            if letter == "0" or letter == "1" or letter == "2" or letter == "3" or letter == "4" or letter == "5" or letter == "6" or letter == "7" or letter == "8" or letter == "9":
                print("Error! This name has a number: " + name)
                return
    print("All names are okay!")

# List from marketing team
names = ["Wofai", "Zainab", "A4atullah"]

# Run the check to see if it is correct
check_names(names)



# List of names from marketing team
names = ["Wofai", "Zainab", "A4atullah", "Joy123", "Peace@", "Love12345"]

# Check each name one by one
good_names = []  
# Look through each name in the list
for name in names:
    # Check if name has only letters (no numbers or symbols)
    has_only_letters = True
    for letter in name:
        if letter not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            has_only_letters = False
            
    if has_only_letters:
        good_names.append(name)
    else:
        print("Found a bad name:", name)

# Show all good names
print("Good names are:")
for name in good_names:
    print(name)