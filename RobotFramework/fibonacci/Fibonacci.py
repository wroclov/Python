def fibonacci(n):
    """
    Generate Fibonacci sequence up to the nth number.
    :param n: int - Number of terms in the Fibonacci sequence to generate.
    :return: list - List containing the Fibonacci sequence or error message.
    """
    try:
        n = int(n)  # Convert input to integer
    except ValueError:
        return "Error: input must be an integer"

    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence
