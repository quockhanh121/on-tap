# Câu 4a (1.5 điểm): Nhập thông tin của máy tính và lưu các thông tin này trong một từ điển

n = int(input("Nhập số lượng máy tính: "))
dict_maytinh = {}

for i in range(n):
    SoHieu = input("Nhập số hiệu máy tính: ")
    BoNho = int(input("Nhập dung lượng bộ nhớ: "))
    OCung = int(input("Nhập dung lượng ổ cứng: "))
    HangSanXuat = input("Nhập hãng sản xuất: ")
    NamSanXuat = int(input("Nhập năm sản xuất: "))
    dict_maytinh[SoHieu] = [BoNho, OCung, HangSanXuat, NamSanXuat]

print(dict_maytinh)
