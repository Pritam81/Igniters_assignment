def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = [line.strip() for line in file.readlines()]
        return lines
    except FileNotFoundError:
        print("Error: File not found.")
        return []

def write_file(file_path, lines):
    try:
        with open(file_path, 'w') as file:
            file.writelines(lines)
    except Exception as e:
        print(f"Error writing to file: {e}")

def solve_expression(expression):
    try:
        expression = expression.replace('^', '**')
        result = eval(expression)
        return result
    except Exception as e:
        return f"Error: {e}"

def process_file(input_path, output_path):
    expressions = read_file(input_path)
    results = []
    
    for expression in expressions:
        if '=' in expression:
            lhs, _ = expression.split('=', 1)
            lhs = lhs.strip()
            result = solve_expression(lhs)
            results.append(f"{lhs} = {result}\n")
        else:
            results.append(f"{expression} = Error: No '=' in expression\n")

    write_file(output_path, results)

def main():
    input_path = input("Enter the path to the input text file: ")
    output_path = input("Enter the path to the output text file: ")
    process_file(input_path, output_path)
    print(f"Results written to {output_path}")

if __name__ == "__main__":
    main()