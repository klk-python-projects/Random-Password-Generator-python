import random
import string

def generate_password(length,characters):
    password = ""
    for i in range(length):
        password += random.choice(characters)
    return password
while True:
    print("\n===== Random Password Generator =====")
    try:
        length = int(input("Enter password length :"))
        if length <= 0:
            print("Password length must be greater than 0.")
        else:
            letters = input("Include Letters ? (yes/no) :").lower()
            numbers = input("Include Numbers ? (yes/no) :").lower()
            symbols = input("Include Symbols ? (yes/no) :").lower()
            invalid = False
            if letters not in ["yes", "no"]:
                print("Invalid choice for Letters.")
                invalid = True
            if numbers not in ["yes", "no"]:
                print("Invalid choice for Numbers.")
                invalid = True
            if symbols not in ["yes", "no"]:
                print("Invalid choice for Symbols.")
                invalid = True
            if invalid == False:
                characters = ""
                if letters == "yes":
                    characters += string.ascii_letters
                if numbers == "yes":
                    characters += string.digits
                if symbols == "yes":
                    characters += string.punctuation
                if characters == "":
                    print("Please select atleast one character type.")
                else:
                    password = generate_password(length,characters)
                    print("\nGenerated Password :", password)
    except ValueError:
        print("Invalid input! Please enter password length in number.")
    
    again = input("Do you want to generate again ? (yes/no) :").lower()
    if again != "yes":
        print("Exit")
        break