import difflib

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = [line.strip() for line in file.readlines()]
        return lines
    except FileNotFoundError:
        print("Error: File not found.")
        return []

def approximate_search(word, strings, k):
    matches = difflib.get_close_matches(word, strings, n=k, cutoff=0)
    return matches

def main():
    print("Welcome to the Approximate Search Program!")
    file_path = input("Enter the path to the text file: ")
    strings = read_file(file_path)

    if not strings:
        return

    print(f"Loaded {len(strings)} strings from the file.")

    while True:
        print("\nEnter a word to search (or type 'exit' to quit):")
        user_input = input("Search: ").strip()

        if user_input.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break

        try:
            k = int(input("Enter the number of suggestions to return (k): "))
        except ValueError:
            print("Invalid input for k. Please enter an integer.")
            continue

        suggestions = approximate_search(user_input, strings, k)

        if suggestions:
            print("\nTop suggestions:")
            for idx, suggestion in enumerate(suggestions, start=1):
                print(f"{idx}. {suggestion}")
        else:
            print("No similar strings found.")

if __name__ == "__main__":
    main()
