def evaluate(first_value: float, second_value: float, third_value: str):
    result = None
    if third_value == '+':
        result = first_value + second_value
    elif third_value == '-':
        result = first_value - second_value
    elif third_value == '*':
        result = first_value * second_value
    elif third_value == '/':
        try:
            result = first_value / second_value
        except ZeroDivisionError:
            return None
    return result