#Câu lệnh if lồng nhau trong python
id_sv = 43
year = 3
if id_sv == 43:
    print("la sv truong y")
    if year == 4:
        print("là sv nam 3")
elif id_sv == 45:
    print("la sv truong neu ")
    if year == 3:
        print("la sv nam cuoi")
else:
    print("la sv truong hust ")
    