#Hãy viết chương trình để thêm danh sách con 
# sub_list = ["h", "i", "j"] vào danh sách gốc 
# list1 và in ra màn hình sao cho thu được đầu ra:
list1= ['a','b', ['c',['d','e',['f','g'],'k'],'l'],'m','n']
sub_list= ['h','i','j']
temp = list1[2][1][2]
temp.extend(sub_list)
print(list1)