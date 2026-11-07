# Câu 5b (1.0 điểm): Tạo 2 đối tượng DienThoai và thực thi phương thức thongtindienthoai()

class DienThoai:
    def __init__(self, MaMay, TenMay, HangSanXuat, DungLuongPin, GiaBan):
        self.MaMay = MaMay
        self.TenMay = TenMay
        self.HangSanXuat = HangSanXuat
        self.DungLuongPin = DungLuongPin
        self.GiaBan = GiaBan

    def thongtindienthoai(self):
        print(f"Mã máy: {self.MaMay}")
        print(f"Tên máy: {self.TenMay}")
        print(f"Hãng sản xuất: {self.HangSanXuat}")
        print(f"Dung lượng pin: {self.DungLuongPin}")
        print(f"Giá bán: {self.GiaBan}")

# b. Tạo 2 đối tượng
DT1 = DienThoai("DT01", "iPhone 15 Pro", "Apple", 3274, 28990000)
DT2 = DienThoai("DT02", "Galaxy S24 Ultra", "Samsung", 5000, 29990000)

# Thực thi phương thức thongtindienthoai()
DT1.thongtindienthoai()
print("-" * 30)
DT2.thongtindienthoai()

