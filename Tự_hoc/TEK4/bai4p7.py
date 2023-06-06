#Lisst sliciting (lấy ra một danh sách con trong list)
#bỏ phần tử cuối cùng nếu nhảy đến
vidu_list=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(vidu_list[:5:2]) # Bỏ trống chỉ số đầu, bước nhảy dương
print(vidu_list[:5:-2]) # Bỏ trống chỉ số đầu, bước nhảy âm
print(vidu_list[5::2]) # Bỏ trống chỉ số cuối, bước nhảy dương
print(vidu_list[5::-2]) # Bỏ trống chỉ số cuối, bước nhảy âm
print(vidu_list[::2]) # Bỏ trống cả chỉ số đầu và cuối, bước nhảy dương
print(vidu_list[::-2]) # Bỏ trống cả chỉ số đầu và cuối, bước nhảy âm
print(vidu_list[::]) # Bỏ trống tất cả các chỉ số và bước nhảy
print(vidu_list[:5]) # Bỏ trống chỉ số đầu và bước nhảy
print(vidu_list[5:]) # Bỏ trống chỉ số cuối và bước nhảy
