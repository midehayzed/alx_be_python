def perform_arithmetic_operations(num1, num2, operation):
    """
    Perform basic arithmetic operations on two numbers.
    
    Parameters:
    num1 (float): The first number.
    num2 (float): The second number.
    operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide').

    Returns:
    float: The result of the arithmetic operation.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        return num1 / num2
    else:
        if num2 == 0:
            return "Error: Division by zero is not allowed."
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (add, subtract, multiply, divide): ").strip()
result = perform_arithmetic_operations(num1, num2, operation)
print(f"Result: {result}")
