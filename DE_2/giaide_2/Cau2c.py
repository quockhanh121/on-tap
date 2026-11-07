# Câu 2c (0.75 điểm): Tính tổng các chữ số trong chuỗi

s = input("Nhập chuỗi s: ")
tong = 0
for i in s:
    if i.isdigit():
        tong += int(i)

print("Tổng các chữ số trong chuỗi: ", tong)

