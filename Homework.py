import ast

def safe_calculator(func):
    def wrapper(expression):
        try:
            ast.parse(expression)
            result = eval(expression)
            return result
        except Exception as e:
            print(f"Error: {e}. Invalid expression: {expression}")
            return None

    return wrapper

@safe_calculator
def calculate(expression):
    return eval(expression)

result = calculate("10 + 10")
print(result)

result = calculate("__import__('os').system('rm -rf /')")
print(result)