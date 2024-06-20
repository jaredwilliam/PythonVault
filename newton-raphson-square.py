# Newton-Raphson for Square Roots


def newton_raphson_square(k: float, epsilon: float = 0.01) -> float:
    """
    Finds an approximation of the square root of 'k'.

    Args:
        k (float): The value to approximate the square root for.
        epsilon (float): Precision to which to find the approximation.

    Returns:
        float: The approximate square root of k
    """
    guess = k / 2

    while abs(guess**2 - k) >= epsilon:
        guess = guess - (((guess**2) - k) / (2 * guess))

    return guess


k = 99
approx = newton_raphson_square(k=k, epsilon=0.001)
print(approx)
