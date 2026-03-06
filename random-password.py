import secrets


def generate_password(length: int, characters: tuple[str, ...]) -> str:
    if length <= 0:
        raise ValueError("Password length must be a positive integer.")
    return "".join(secrets.choice(characters) for _ in range(length))


def main():
    characters = tuple("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()")

    while True:
        try:
            password_length = int(input("Enter the desired password length: "))
            password = generate_password(password_length, characters)
        except ValueError:
            print("Please enter a positive integer for the password length.")
            continue

        print(f"Generated password: {password}")

        again = input("Do you want to generate another password? (yes/no): ").strip().lower()
        if again not in {"yes", "y"}:
            break


main()