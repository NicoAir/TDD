def add(numbers: str) -> int:
    if not numbers:
        return 0
    else:
        numbers_list = numbers.split(',')
        return sum(int(num) for num in numbers_list)