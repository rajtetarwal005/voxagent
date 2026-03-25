from langchain.tools import tool

@tool
def calculator(expression: str) -> str:
    """Evaluate mathematical expressions"""
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"


# test (temporary)
if __name__ == "__main__":
    print(calculator.invoke("5 * 10 + 3"))