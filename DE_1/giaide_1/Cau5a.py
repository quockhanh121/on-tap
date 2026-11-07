# Câu 5a (1.0 điểm): Tạo lớp MonHoc với các thuộc tính và phương thức

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
