a = 100
b = float("200.5")
print(a+b)
# Trong chương trình trên chúng ta thực hiện thêm biến a và b. Chúng ta đã chuyển đổi biến b từ kiểu chuỗi (cao hơn) sang kiểu số thực dạng thập phân (thấp hơn) bằng cách sưr dụng ham float(). Sau ki chuyển đổi thành một giá trị số thập phân, Python có thể trực tiếp thực hiện phép cộng cho hai biến này. Kết quả ta nhận được là một số thập phân
# Việc chuyển dổi kiểu dữ liệu bắt buộc này rất cần thiết đặc biệt khi chúng ta nhớ lại bài về hàm input(). Bất cứ thứ kiểu dữ liệu đầu vào nào, hàm input() sẽ chuyển đổi nó thnahf một chuỗi ký tự. Nếu bạn nhập một giá trị nguyên, hàm input()sẽ chuyển thành một chuỗi ký tự có chứa ố nguyên đó. Do đó, đẻ sử dụng được như số nguyên hoặc số thực bạn cần thực hiện việc chuyển đổi trực tiếp nó thành dạng dữu liệu mong muốn bằng cách sử dụng tính năng ép kiểu
