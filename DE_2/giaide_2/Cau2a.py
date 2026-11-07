# Câu 2a (0.75 điểm): Đếm số ký tự chữ hoa có trong chuỗi

s = input("Nhập chuỗi s: ")
dem = 0
for i in s:
    if i.isupper():
        dem += 1

if dem == 0:
    print("Chuỗi không có ký tự chữ hoa.")
else:
    print("Số ký tự chữ hoa: ", dem)

