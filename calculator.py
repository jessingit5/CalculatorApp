def add (n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0: 
        raise ValueError("Cannot divide by zero")
    return n1 / n2

if __name__ == "__main__":
    operations = {
        "+": add,
        "-": substract,
        "*": multiply,
        "/": divide
    }

    num1 = float(input("What is the first number: "))
    for symbol in operations:
        print(symbol)
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What is the second number: "))
    

    calculation_function = operations.get(operation_symbol)
    
    if calculation_function:
        try:
            answer = calculation_function(num1, num2)
            print(f"{num1} {operation_symbol} {num2} = {answer}")
        except ValueError as e:
            print(f"Error: {e}")
    else:
        print("Invalid operation selected.")