def calculateAverage(numbers):
    if not numbers:
        raise ValueError("The input list cannot be empty")
    total_sum = sum(numbers)
    count = len(numbers)
    average = total_sum / count
    return average

