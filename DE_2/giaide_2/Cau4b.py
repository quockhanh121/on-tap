# Câu 4b (0.5 điểm): Nhập mã số sách, nếu tồn tại thì xóa khỏi từ điển, ngược lại thông báo không tìm thấy

from datetime import datetime

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

print("\nTừ điển sách ban đầu:", tudien)

# b. Xóa cuốn sách theo mã số
x = input("Nhập mã số sách cần xóa: ")
if x in tudien:
    del tudien[x]
    print(f"Cuốn sách có mã số {x} đã được xóa.")
else:
    print("Không tìm thấy cuốn sách cần xóa.")

print("Từ điển sách sau khi cập nhật:", tudien)

