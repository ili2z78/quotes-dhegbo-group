
from functions import add_quote

def menu():
    print("1. Display Quotes")
    print("2. Add Quote")
    print("3. Quit")
    choice = input("Enter your choice (1/2/3): ")
    return choice

def main():
    filename = "quotes.txt"  
    quotes = []

    try:
        with open(filename, 'r') as file:
            quotes = file.readlines()
    except FileNotFoundError:
        pass

    while True:
        choice = menu()

        if choice == '1':
            print("Quotes:")
            for quote in quotes:
                print(quote.strip())  
        elif choice == '2':
            add_quote(quotes, filename)
            print("Quote added successfully!")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
