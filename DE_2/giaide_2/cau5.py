# Câu 5 (2.0 điểm)

# a. Lớp DienThoai (1.0 điểm)
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

# b. Khởi tạo 2 đối tượng và gọi thongtindienthoai() (1.0 điểm)
DT1 = DienThoai("DT01", "iPhone 15 Pro", "Apple", 3274, 28990000)
DT2 = DienThoai("DT02", "Galaxy S24 Ultra", "Samsung", 5000, 29990000)

DT1.thongtindienthoai()
DT2.thongtindienthoai()

