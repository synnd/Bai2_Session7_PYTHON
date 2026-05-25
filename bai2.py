# Đoạn code bị sai
# transaction =" nguyEN van a | PYTHON-01 | 15000000 | paid "
# transaction.strip()
# parts = transaction.split("-")
# student_name = parts[0].title()
# course_code = parts[1]
# amount = parts[2]
# status = parts[3].upper()
# print("Học viên:", student_name)
# print("Khóa học:", course_code)
# print("Sô tiên:", amount, "VND")
# print("Trạng thái:", status)

#  transaction.strip() không thay đổi chuỗi ban đầu vì strip trả về chuỗi mới chứ không thy đổi trực tiếp chuỗi ban đầu
# Chuỗi giao dịch thực tế được phân cách bằng ký tự | 
#  transaction.split("-") là sai vì nó không pk chuỗi phân cách chính trong mẫu dữ liệu
# Khi split sai:
# parts[0] => " nguyEN van a | PYTHON"
# parts[1] => "01 | 15000000 | paid "
# => dữ liệu bị lệch cột.
# Cần .strip() từng phần để xóa khoảng trắng thừa sau khi tách dữ liệu.
# cần đổi amount sang số để định dạng tiền đúng, tính toán được, tránh lỗi kiểu dữ liệu
transaction = " nguyEN van a | PYTHON-01 | 15000000 | paid "
transaction = transaction.strip()

parts = transaction.split("|")

student_name = parts[0].strip().title()
course_code = parts[1].strip()
amount = int(parts[2].strip())
status = parts[3].strip().upper()


print("Học viên:", student_name)
print("Khóa học:", course_code)
print("Số tiền:", format(amount, ","), "VND")
print("Trạng thái:", status)
