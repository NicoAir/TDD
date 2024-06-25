def add(numbers: str) -> int:
    if not numbers:
        return 0
    else:
        numbers_list = numbers.split(',')
        if len(numbers_list) > 2:
            raise ValueError("Input string can only contain up to two numbers")
        return sum(int(num) for num in numbers_list)