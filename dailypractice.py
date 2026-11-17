def is_armstrong(num):
    # Convert number to a string to calculate the number of digits
    n = len(str(num))

    # Calculate the sum of each digit raised to the power of n
    sum_of_powers = sum(int(digit) ** n for digit in str(num))

    # Check if the sum equals the original number
    return sum_of_powers == num
