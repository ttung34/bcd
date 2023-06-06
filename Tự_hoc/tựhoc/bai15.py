 #một số hàm xử lý với string p2
name = "trinh thanh tung la tung hoc cong nghe thong tin"
#s.find() Tìm kiếm từ trong 1 chuỗi
name.find("tung")
name.find("tung",5)
name.find("tùng",5,24)
'nguyen' in name #kiểm tra từ có trong một chuỗi hay không
'cong' in name
#s.index() lấy ra vị trí của một từ đang tìm
name.index("thanh tung")
name.index("thong tin")
#s.replace()Tìm thay thế từ
name.replace("thanh tung","thao nguyen")
#s.isalnum()Trả về true nếu chuối có ít nhất 1 ký tự
name.isalnum()
#s.isalpha Trả về true nếu chuối không có khoảng trắng và ký tự đặc biệt
name.isalpha()
#s.isdigit()Trả về true nếu chuỗi là số
name.isdigit()
#s.isspace()Trả về true nếu chuối là khoảng trắng
name.isspace()
