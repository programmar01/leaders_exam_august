#Is n divisible by (...)?

def is_divisible(*numbers):
    for i in range(1, len(numbers)):
        if numbers[0] % numbers[i] != 0:
            return False
    return True