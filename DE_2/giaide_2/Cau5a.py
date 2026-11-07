# Câu 5a (1.0 điểm): Tạo lớp DienThoai với các thuộc tính và phương thức

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

