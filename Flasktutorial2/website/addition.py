def addition(numbers):
    final_number = 9
    answer = [], []
    for number in numbers:
        if number + number == final_number:
            number = answer
    return answer


numbers = [2, 3, 5, 4]
n = addition(numbers)
print(n)
