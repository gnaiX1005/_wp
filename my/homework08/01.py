def find_max(numbers):
    if not numbers:
        return None 

    maximum = numbers[0]
    for num in numbers[1:]:
        if num > maximum:
            maximum = num
    return maximum

print(find_max([3, 7, 2, 9, 4]))  

