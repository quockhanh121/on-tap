# Câu 4 (2.0 điểm)
from datetime import datetime

# a. Nhập thông tin của các cuốn sách trong thư viện (1.5 điểm)
n = int(input("Nhập số lượng sách (n>0): "))
while n <= 0:
    n = int(input("Nhập số lượng sách (n>0): "))

tudien = {}
namhientai = datetime.now().year

for i in range(n):
    MaSoSach = input("Nhập mã số sách: ")
    TenSach = input("Nhập tên sách: ")
    TenTacGia = input("Nhập tên tác giả: ")
    NhaXuatBan = input("Nhập nhà xuất bản: ")
    NamXuatBan = int(input("Nhập năm xuất bản: "))
    while NamXuatBan > namhientai:
        NamXuatBan = int(input(f"Năm xuất bản không hợp lệ, vui lòng nhập năm <= {namhientai}: "))
    tudien[MaSoSach] = [TenSach, TenTacGia, NhaXuatBan, NamXuatBan]

print("Từ điển sách:", tudien)

# b. Nhập mã số sách cần tìm để xóa (0.5 điểm)
x = input("Nhập mã số sách cần xóa: ")
if x in tudien:
    del tudien[x]
    print(f"Cuốn sách có mã số {x} đã được xóa.")
else:
    print("Không tìm thấy cuốn sách cần xóa.")

print("Từ điển sách sau khi cập nhật:", tudien)

