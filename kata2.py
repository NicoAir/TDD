import re 

def add(numbers: str) -> int:
    if not numbers:
        return 0
    else:
        numbers_list = re.split(',|\n', numbers)
        return sum(int(num) for num in numbers_list)