def so_can_tim(a,b):
    print(f"Below are all perfect numbers between{a} and {b}")
    for num in range(a,b+1):
        sum_dt = 0
        for i in range(num):
            if num %i == 0:
                sum_dt+=1
        if sum_dt == num:
            print(f'{num} la so hoan hao')
a= input()
b= input()
so_can_tim(a,b) 