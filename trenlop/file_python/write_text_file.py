# 1.1 Cách ghi file text {.txt}
# các bước:
   #B1: Mở file: open ()- mode: "w"-ghi(ghi đề lên nội dung), "a"-ghi(ghi nối vào cái có sẵn)
   #B2: Ghi file, đọc dữ liệu: 
   # write(): Ghi một chuỗi vào file 'tùng'
   # writelines(): Ghi  một list kiểu chuỗi vào file['a','b']
   #B3: Đóng luồng(file): close() - with( tự động đóng)
   
lines = ['Python', 'Java', 'PHP']

with open('C:\\Users\\admin\\OneDrive\\Máy tính\\text.txt\\text.txt', 'w', encoding='utf-8') as f:
    f.writelines(lines)
    print(f)
