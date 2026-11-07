# Câu 4a (1.5 điểm): Nhập thông tin của các cuốn sách trong thư viện và lưu trong một từ điển

from datetime import datetime

n = int(input("Nhập số lượng sách (n>0): "))
while n <= 0:
    n = int(input("Nhập số lượng sách (n>0): "))

tudien = {}
namhientai = datetime.now().year

for i in range(n):
    print(f"\n--- Nhập cuốn sách thứ {i + 1} ---")
    MaSoSach = input("Nhập mã số sách: ")
    TenSach = input("Nhập tên sách: ")
    TenTacGia = input("Nhập tên tác giả: ")
    NhaXuatBan = input("Nhập nhà xuất bản: ")
    NamXuatBan = int(input("Nhập năm xuất bản: "))
    while NamXuatBan > namhientai:
        NamXuatBan = int(input(f"Năm xuất bản không hợp lệ, vui lòng nhập năm <= {namhientai}: "))
    tudien[MaSoSach] = [TenSach, TenTacGia, NhaXuatBan, NamXuatBan]

print("\nTừ điển sách trong thư viện:")
print(tudien)

