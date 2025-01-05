# README: Python Programs by Pritam

This README provides detailed explanations for four Python programs written by me, Pritam. Each program demonstrates problem-solving skills and a clear understanding of core programming concepts. Below, you'll find descriptions, features, instructions for running the programs, and other relevant details.

---

## 1. **Approximate Search Program**

### Overview
The Approximate Search program reads a text file containing strings, stores them in memory, and allows the user to search for strings that are most similar to a given input string. This program uses fuzzy matching to return the top K similar strings based on their similarity score.

### Features
- Reads strings from a text file.
- Performs approximate search using the `difflib` module.
- Interactive interface for users to enter search queries.
- Customizable number of suggestions (K).

### How to Run
1. Save the program in a file named `approximate_search.py`.
2. Prepare a text file with strings (one per line).
3. Run the program using Python:
   ```bash
   python approximate_search.py
   ```
4. Follow the prompts to provide the file path and perform searches.

---

## 2. **Arithmetic Expression Solver**

### Overview
This program reads a text file containing arithmetic expressions, solves each expression, and writes the results to a new file. The expressions are expected to have an equals sign (`=`) at the end, and the program fills in the correct result.

### Features
- Reads arithmetic expressions from a text file.
- Solves complex expressions using `eval()`.
- Supports operators `+`, `-`, `*`, `/`, `^` and parentheses.
- Outputs results to a new file.

### How to Run
1. Save the program in a file named `solve_arithmetic.py`.
2. Prepare an input text file with arithmetic expressions (e.g., `input.txt`).
3. Run the program:
   ```bash
   python solve_arithmetic.py
   ```
4. Enter the input and output file paths when prompted.
5. Check the output file for results.

---

## 3. **Email Sender Program**

### Overview
This program sends an email with a predefined subject and body, along with an image attachment. It ensures only valid image formats (PNG, JPG, JPEG) are allowed.

### Features
- Sends emails via Gmail's SMTP server.
- Accepts user credentials for secure authentication.
- Validates image attachments before sending.

### How to Run
1. Save the program in a file named `send_email.py`.
2. Ensure you have a Gmail account and enable "Less secure app access" or use an app password.
3. Run the program:
   ```bash
   python send_email.py
   ```
4. Follow the prompts to provide sender email, password, and recipient details.
5. Provide the path to the image attachment.

**Note:** Modify the SMTP settings if using a non-Gmail provider.

---

## 4. **Palindrome Checker**

### Overview
This program checks whether a given string is a palindrome, ignoring case, spaces, and special characters.

### Features
- Normalizes input by removing non-alphanumeric characters and converting to lowercase.
- Compares the string with its reverse to check for palindromes.
- Simple and interactive user interface.

### How to Run
1. Save the program in a file named `palindrome_check.py`.
2. Run the program:
   ```bash
   python palindrome_check.py
   ```
3. Enter a string when prompted, and the program will determine if it is a palindrome.

---

## General Requirements
- Python 3.x installed on your system.
- For the Email Sender program, an active internet connection and a valid email account are required.

## Conclusion
These programs showcase my skills in Python programming, problem-solving, and implementing interactive applications. Each program is designed to address a specific challenge and can be extended or modified for additional features.

If you have any questions or suggestions, feel free to reach out!

