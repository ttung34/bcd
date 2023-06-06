five_numbers = []
k_number = 1

while len(five_numbers)<6:
    k_number +=1
    if k_number %2 != 0:
        five_numbers.append(k_number)
        continue
    print(five_numbers)
        