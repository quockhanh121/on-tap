# Câu 4b (0.5 điểm): Nhập số hiệu máy tính, nếu tồn tại thì xóa khỏi từ điển, ngược lại thông báo không có

n = int(input("Nhập số lượng máy tính: "))
dict_maytinh = {}

for i in range(n):
    SoHieu = input("Nhập số hiệu máy tính: ")
    BoNho = int(input("Nhập dung lượng bộ nhớ: "))
    OCung = int(input("Nhập dung lượng ổ cứng: "))
    HangSanXuat = input("Nhập hãng sản xuất: ")
    NamSanXuat = int(input("Nhập năm sản xuất: "))
    dict_maytinh[SoHieu] = [BoNho, OCung, HangSanXuat, NamSanXuat]

x = input("Nhập số hiệu máy tính cần tìm: ")
if x in dict_maytinh:
    del dict_maytinh[x]
    print(f"Máy tính có số hiệu {x} đã được xóa.")
else:
    print("Không có số hiệu máy tính cần xóa.")

print(dict_maytinh)
