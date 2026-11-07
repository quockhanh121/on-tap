# Câu 2 (2.0 điểm)
s = input("Nhập chuỗi s: ")

# a. Đếm số ký tự chữ hoa có trong chuỗi (0.75 điểm)
dem = 0
for i in s:
    if i.isupper():
        dem += 1

if dem == 0:
    print("Chuỗi không có ký tự chữ hoa.")
else:
    print("Số ký tự chữ hoa:", dem)

# b. Kiểm tra xem chuỗi s có đối xứng hay không (0.5 điểm)
def DoiXung(s):
    if s == s[::-1]:
        print("Chuỗi đối xứng.")
    else:
        print("Chuỗi không đối xứng.")

DoiXung(s)

# c. Tính tổng các chữ số trong chuỗi (0.75 điểm)
tong = 0
for i in s:
    if i.isdigit():
        tong += int(i)

print("Tổng các chữ số trong chuỗi:", tong)

