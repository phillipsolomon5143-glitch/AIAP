def compute_stats(numbers):
    """
    Compute basic statistics (mean, maximum, minimum) of a list of numbers.

    Args:
        numbers (list of float or int): A list of numeric values.

    Returns:
        tuple: A tuple containing:
            - mean (float): The arithmetic mean of the numbers.
            - maximum (float or int): The largest number in the list.
            - minimum (float or int): The smallest number in the list.

    Raises:
        ValueError: If the input list is empty.
    """
    if not numbers:
        raise ValueError("Input list must not be empty")

    # Calculate the sum of all numbers
    total_sum = sum(numbers)
    
    # Calculate the number of elements
    count = len(numbers)
    
    # Compute the mean
    mean = total_sum / count
    
    # Find the maximum value
    maximum = max(numbers)
    
    # Find the minimum value
    minimum = min(numbers)
    
    return mean, maximum, minimum
