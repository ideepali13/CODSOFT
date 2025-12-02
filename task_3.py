import random
import string

def generate_password(length):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choices(all_chars, k=length))
    return password

def password_generator_app():
    print("=========================================")
    print("        ** Password Generator **         ")
    print("=========================================")

    while True:
        try:
            length_input = input("Enter the desired password length: ")
            password_length = int(length_input)

            if password_length <= 0:
                print("Password length must be a positive number. Please try again.")
            else:
                generated_password = generate_password(password_length)
                print("\n" + "="*40)
                print(f"Generated Password (Length: {len(generated_password)}):")
                print(f"**{generated_password}**")
                print("="*40 + "\n")
                break

        except ValueError:
            print("Invalid input. Please enter a valid whole number for the length.")

if __name__ == "__main__":
    password_generator_app()