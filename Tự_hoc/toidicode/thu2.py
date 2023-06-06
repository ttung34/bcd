def a(x):
    if x%x == 1 and x%1 == x:
        return "x la số nguyên tố"
    else:
        return "x không phải là số nguyên tố"
    
y = a(7)
print(y)