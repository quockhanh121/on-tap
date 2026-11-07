# Câu 5b (1.0 điểm): Tạo 2 đối tượng MonHoc và thực thi phương thức thongtinmonhoc()

class MonHoc:
    def __init__(self, MaMonHoc, TenMonHoc, SoTinChi, KhoaPhuTrach):
        self.MaMonHoc = MaMonHoc
        self.TenMonHoc = TenMonHoc
        self.SoTinChi = SoTinChi
        self.KhoaPhuTrach = KhoaPhuTrach

    def thongtinmonhoc(self):
        print(f"Mã môn học: {self.MaMonHoc}")
        print(f"Tên môn học: {self.TenMonHoc}")
        print(f"Số tín chỉ: {self.SoTinChi}")
        print(f"Khoa phụ trách: {self.KhoaPhuTrach}")

# Tạo 2 đối tượng
CSDL = MonHoc(229008, "Cơ sở dữ liệu", 3, "Công nghệ thông tin")
TA1 = MonHoc(224604, "Tiếng Anh 1", 2, "Ngoại ngữ")

# Thực thi phương thức thongtinmonhoc()
CSDL.thongtinmonhoc()
TA1.thongtinmonhoc()
