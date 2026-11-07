# Câu 2a (1.0 điểm): Đếm số ký tự chữ thường có trong chuỗi s

s = input("Nhập chuỗi s: ")
dem = 0
for i in s:
    if i.islower():
        dem += 1

if dem == 0:
    print("Chuỗi không có ký tự chữ thường.")
else:
    print("Số ký tự chữ thường trong chuỗi: ", dem)
