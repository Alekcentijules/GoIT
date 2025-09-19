from joke import get_random_joke

def main():
    name = input("Enter a name, please: ")
    print(f"Bonjour, {name}!")
    var = True

    while var == True:
        user_response = input(f"{name}, would you like to hear a joke? (yes/no): ").lower()
        if user_response == "yes":
            print(get_random_joke())
        elif user_response == "no":
            print(f"Auf Wiedersehen, {name}!")
            var = False

if __name__ == "__main__":
    main()