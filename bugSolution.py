def function_with_uncommon_error(x):
    try:
        if x == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        else:
            return 1 / x
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        return None  # Or handle the error as needed