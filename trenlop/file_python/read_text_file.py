# Nội dung 
# 1. Cách đọc - ghi file text 
# 2. Cách đọc - ghi file csv

# 1.1 Cách đọc file text {.txt}
# các bước:
   #B1: Mở file: open ()- mode(chế độ): 'r'-đọc, "w"-ghi(ghi đề lên nội dung), "a"-ghi(ghi nối vào cái có sẵn)
   #B2: Đọc file, đọc dữ liệu: read (đọc 1 ký tự), redline (đọc một dòng), readlines (đọc nhiều dòng)
   #B3: Đóng luồng(file): close() - with( tự động đóng)
    
    
   
  

with open('C:\\Users\\admin\\OneDrive\\Máy tính\\text.txt\\text.txt', 'r', encoding='utf-8') as f:
   contents = f.readlines()
   print(contents)