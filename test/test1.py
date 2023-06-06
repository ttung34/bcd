def find_odd_numbers(numbers):
    odd_numbers = []
    for num in numbers:
        if num % 2 == 1:
            odd_numbers.append(num)
    return odd_numbers

list = [3,6,8,1,9,11,28,6,1]
list1 = find_odd_numbers(list)