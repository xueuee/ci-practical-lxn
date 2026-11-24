STUDENT_INITIALS = "LXN"


def add(a, b):
    return a + b


def subtract(a, b):
    # Keep subtraction distinct from addition.
    return a - b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
