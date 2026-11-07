# -*- coding: utf-8 -*-
"""
HỆ THỐNG CHẤM ĐIỂM TỰ ĐỘNG BÀI THI PYTHON - ĐỀ 1 (CA THI 9H45)
Trường Cao Đẳng Công Thương TP.HCM - Khoa Công Nghệ Thông Tin
Mã đề thi: 11301 - Thang điểm chuẩn: 10.0
"""

import sys
import subprocess
import os
import datetime

# Kích hoạt hỗ trợ ANSI màu sắc trên console Windows
if sys.platform == "win32":
    try:
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
        os.system('')  # Bật chế độ VT100 cho CMD/PowerShell
    except Exception:
        pass

# Định nghĩa bảng màu Terminal
class C:
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    DIM     = "\033[2m"
    RED     = "\033[91m"
    GREEN   = "\033[92m"
    YELLOW  = "\033[93m"
    BLUE    = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN    = "\033[96m"
    WHITE   = "\033[97m"
    BG_GREEN = "\033[42m\033[30m"
    BG_RED   = "\033[41m\033[37m"
    BG_BLUE  = "\033[44m\033[37m"

DIR_PATH = os.path.dirname(os.path.abspath(__file__))

def find_file(filename):
    """Tìm file trong thư mục hiện tại hoặc các thư mục con (giaide_1, code,...)"""
    direct_path = os.path.join(DIR_PATH, filename)
    if os.path.exists(direct_path):
        return direct_path
    for root, dirs, files in os.walk(DIR_PATH):
        if filename in files:
            return os.path.join(root, filename)
    return None

def run_script(filename, input_data="", timeout=3):
    """Thực thi file code Python an toàn với timeout và UTF-8"""
    filepath = find_file(filename)
    if not filepath or not os.path.exists(filepath):
        return None, "", f"File '{filename}' không tồn tại trong thư mục."
    try:
        env = os.environ.copy()
        env["PYTHONIOENCODING"] = "utf-8"
        proc = subprocess.run(
            [sys.executable, filepath],
            input=input_data,
            text=True,
            capture_output=True,
            timeout=timeout,
            encoding='utf-8',
            errors='replace',
            env=env,
            cwd=os.path.dirname(filepath)
        )
        return proc.returncode, proc.stdout, proc.stderr
    except subprocess.TimeoutExpired:
        return -1, "", "Hết thời gian chờ (Vòng lặp vô tận while/for)."
    except Exception as e:
        return -2, "", str(e)


# ==============================================================================
# BỘ TEST CASES CHI TIẾT (TỔNG 10.0 ĐIỂM)
# ==============================================================================

def test_Cau1a():
    """Câu 1a (0.5đ): n ngoài [1; 99] yêu cầu nhập lại"""
    ret, out, err = run_script("Cau1a.py", input_data="-10\n150\n25\n")
    if ret == 0:
        out_l = out.lower()
        if ("nhập lại" in out_l or out_l.count("nhập") >= 3) and "25" in out:
            return 0.5, "Bắt nhập lại khi n ngoài [1;99] chuẩn xác."
        elif "25" in out:
            return 0.25, "Nhập được n=25 nhưng chưa in rõ thông báo nhập lại."
    return 0.0, f"Lỗi chạy file: {err or out}"

def test_Cau1b():
    """Câu 1b (0.75đ): Hàm tính tổng ước số của n. n=12 -> 28, n=6 -> 12"""
    ret1, out1, err1 = run_script("Cau1b.py", input_data="12\n")
    ret2, out2, err2 = run_script("Cau1b.py", input_data="6\n")
    score = 0.0
    if ret1 == 0 and "28" in out1:
        score += 0.45
    if ret2 == 0 and "12" in out2:
        score += 0.30
    if score >= 0.75:
        return 0.75, "Hàm TongUocSo tính chuẩn (12->28, 6->12)."
    elif score > 0:
        return score, "Tính đúng một số trường hợp ước số."
    return 0.0, f"Lỗi tính ước số: {err1 or out1}"

def test_Cau1c():
    """Câu 1c (0.75đ): S = 1 + 2^2 + ... + n^n. n=3 -> 32, n=1 -> 1"""
    ret1, out1, err1 = run_script("Cau1c.py", input_data="3\n")
    ret2, out2, err2 = run_script("Cau1c.py", input_data="1\n")
    score = 0.0
    if ret1 == 0 and "32" in out1:
        score += 0.50
    if ret2 == 0 and (" 1" in out2 or "=1" in out2 or "= 1" in out2):
        score += 0.25
    if score >= 0.75:
        return 0.75, "Hàm S(n) tính lũy thừa chính xác (n=3 -> 32)."
    elif score > 0:
        return score, "Có tính S nhưng kết quả chưa trọn vẹn."
    return 0.0, f"Lỗi tính S: {err1 or out1}"

def test_Cau2a():
    """Câu 2a (1.0đ): Đếm số ký tự chữ thường"""
    ret1, out1, err1 = run_script("Cau2a.py", input_data="Hello World\n")
    ret2, out2, err2 = run_script("Cau2a.py", input_data="PYTHON\n")
    score = 0.0
    if ret1 == 0 and "8" in out1:
        score += 0.6
    if ret2 == 0 and ("không có ký tự chữ thường" in out2.lower() or "0" in out2):
        score += 0.4
    if score == 1.0:
        return 1.0, "Đếm ký tự thường và xử lý khi không có rất tốt."
    elif score > 0:
        return score, "Đếm được ký tự thường ở một số trường hợp."
    return 0.0, f"Lỗi đếm ký tự thường: {err1 or out1}"

def test_Cau2b():
    """Câu 2b (0.5đ): Kiểm tra chuỗi đối xứng"""
    ret1, out1, err1 = run_script("Cau2b.py", input_data="madam\n")
    ret2, out2, err2 = run_script("Cau2b.py", input_data="python\n")
    if ret1 == 0 and ret2 == 0:
        is_sym = "chuỗi đối xứng" in out1.lower()
        is_not = "chuỗi không đối xứng" in out2.lower()
        if is_sym and is_not:
            return 0.5, "Nhận diện cả chuỗi đối xứng và không đối xứng đúng."
        elif is_sym:
            return 0.25, "Nhận diện được đối xứng, thiếu kiểm tra không đối xứng."
    return 0.0, f"Lỗi kiểm tra đối xứng: {err1 or out1}"

def test_Cau2c():
    """Câu 2c (0.5đ): Đổi ký tự đầu tiên mỗi từ thành chữ hoa"""
    ret, out, err = run_script("Cau2c.py", input_data="lap trinh python\n")
    if ret == 0 and "Lap Trinh Python" in out:
        return 0.5, "Đổi chữ hoa đầu mỗi từ thành công (Lap Trinh Python)."
    return 0.0, f"Lỗi đổi chữ hoa: {err or out}"

def test_Cau3a():
    """Câu 3a (0.75đ): Nhập danh sách dừng khi nhập 0, in danh sách"""
    ret, out, err = run_script("Cau3a.py", input_data="10\n-5\n8\n0\n")
    if ret == 0 and "[" in out and "]" in out and "10" in out and "-5" in out and "8" in out:
        return 0.75, "Nhập danh sách dừng khi gặp 0 và in đúng [10, -5, 8]."
    elif ret == 0 and "[" in out:
        return 0.4, "Có in danh sách nhưng chưa đầy đủ phần tử."
    return 0.0, f"Lỗi nhập danh sách: {err or out}"

def test_Cau3b():
    """Câu 3b (0.75đ): In ra các số dương chẵn trong danh sách"""
    ret1, out1, err1 = run_script("Cau3b.py", input_data="2\n-4\n6\n7\n0\n")
    ret2, out2, err2 = run_script("Cau3b.py", input_data="-2\n3\n5\n0\n")
    score = 0.0
    if ret1 == 0 and "2" in out1 and "6" in out1 and "-4" not in out1.replace("[-4", ""):
        score += 0.50
    if ret2 == 0 and ("không có số dương chẵn" in out2.lower() or "[]" in out2):
        score += 0.25
    if score >= 0.75:
        return 0.75, "Lọc và in đúng các số dương chẵn (loại số âm, số lẻ)."
    elif score > 0:
        return score, "Lọc được số dương chẵn cơ bản."
    return 0.0, f"Lỗi lọc số dương chẵn: {err1 or out1}"

def test_Cau3c():
    """Câu 3c (0.5đ): Đếm số lần xuất hiện của k trong danh sách"""
    ret1, out1, err1 = run_script("Cau3c.py", input_data="5\n2\n5\n5\n0\n5\n")
    ret2, out2, err2 = run_script("Cau3c.py", input_data="1\n2\n3\n0\n9\n")
    score = 0.0
    if ret1 == 0 and ("3 lần" in out1.lower() or ("xuất hiện" in out1.lower() and "3" in out1)):
        score += 0.35
    if ret2 == 0 and ("không có" in out2.lower() or "0" in out2):
        score += 0.15
    if score >= 0.5:
        return 0.5, "Đếm số lần xuất hiện của k chính xác (k=5 ra 3 lần)."
    elif score > 0:
        return score, "Đếm k đúng một phần."
    return 0.0, f"Lỗi đếm k: {err1 or out1}"

def test_Cau4a():
    """Câu 4a (1.5đ): Nhập thông tin máy tính lưu vào từ điển"""
    input_str = "1\nMT01\n16\n512\nDell\n2023\n"
    ret, out, err = run_script("Cau4a.py", input_data=input_str)
    if ret == 0 and "{" in out and "}" in out and "MT01" in out and ("Dell" in out or "16" in out):
        return 1.5, "Nhập và lưu cấu trúc từ điển máy tính hoàn chỉnh."
    elif ret == 0 and "{" in out:
        return 0.8, "Có tạo từ điển nhưng chưa đủ thông tin."
    return 0.0, f"Lỗi từ điển máy tính: {err or out}"

def test_Cau4b():
    """Câu 4b (0.5đ): Xóa máy tính theo số hiệu"""
    input_str1 = "1\nMT01\n16\n512\nDell\n2023\nMT01\n"
    input_str2 = "1\nMT01\n16\n512\nDell\n2023\nMT99\n"
    ret1, out1, err1 = run_script("Cau4b.py", input_data=input_str1)
    ret2, out2, err2 = run_script("Cau4b.py", input_data=input_str2)
    score = 0.0
    if ret1 == 0 and ("đã được xóa" in out1.lower() or "xóa" in out1.lower()):
        score += 0.35
    if ret2 == 0 and ("không có" in out2.lower() or "không tìm thấy" in out2.lower()):
        score += 0.15
    if score >= 0.5:
        return 0.5, "Xóa máy tính có trong từ điển và báo khi không có."
    elif score > 0:
        return score, "Xử lý xóa máy tính cơ bản."
    return 0.0, f"Lỗi xóa máy tính: {err1 or out1}"

def test_Cau5a():
    """Câu 5a (1.0đ): Khai báo lớp MonHoc"""
    filepath = find_file("Cau5a.py")
    if not filepath or not os.path.exists(filepath):
        return 0.0, "File Cau5a.py không tồn tại."
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            code = f.read()
        if "class MonHoc" in code and "def __init__" in code and "thongtinmonhoc" in code:
            return 1.0, "Khai báo lớp MonHoc, __init__ và thongtinmonhoc đầy đủ."
        return 0.5, "Lớp MonHoc chưa đủ phương thức yêu cầu."
    except Exception as e:
        return 0.0, f"Lỗi đọc file Cau5a.py: {e}"

def test_Cau5b():
    """Câu 5b (1.0đ): Khởi tạo 2 đối tượng môn học và in thông tin"""
    ret, out, err = run_script("Cau5b.py", input_data="")
    if ret == 0:
        has_m1 = "229008" in out and ("Cơ sở dữ liệu" in out or "co so du lieu" in out.lower())
        has_m2 = "224604" in out and ("Tiếng Anh 1" in out or "tieng anh" in out.lower())
        if has_m1 and has_m2:
            return 1.0, "Khởi tạo 2 đối tượng môn học và gọi thongtinmonhoc() chuẩn."
        elif has_m1 or has_m2:
            return 0.5, "Đã in được thông tin của 1 đối tượng."
    return 0.0, f"Lỗi khởi tạo đối tượng môn học: {err or out}"


# ==============================================================================
# GIAO DIỆN HIỂN THỊ & XUẤT PHIẾU ĐIỂM
# ==============================================================================

DANH_SACH_BAI = [
    ("Câu 1a", "Cau1a.py", 0.5, test_Cau1a),
    ("Câu 1b", "Cau1b.py", 0.75, test_Cau1b),
    ("Câu 1c", "Cau1c.py", 0.75, test_Cau1c),
    ("Câu 2a", "Cau2a.py", 1.0, test_Cau2a),
    ("Câu 2b", "Cau2b.py", 0.5, test_Cau2b),
    ("Câu 2c", "Cau2c.py", 0.5, test_Cau2c),
    ("Câu 3a", "Cau3a.py", 0.75, test_Cau3a),
    ("Câu 3b", "Cau3b.py", 0.75, test_Cau3b),
    ("Câu 3c", "Cau3c.py", 0.5, test_Cau3c),
    ("Câu 4a", "Cau4a.py", 1.5, test_Cau4a),
    ("Câu 4b", "Cau4b.py", 0.5, test_Cau4b),
    ("Câu 5a", "Cau5a.py", 1.0, test_Cau5a),
    ("Câu 5b", "Cau5b.py", 1.0, test_Cau5b),
]

def in_header():
    print(C.CYAN + C.BOLD + "╔" + "═" * 76 + "╗" + C.RESET)
    print(C.CYAN + C.BOLD + "║" + " TRƯỜNG CAO ĐẲNG CÔNG THƯƠNG TP.HCM - KHOA CÔNG NGHỆ THÔNG TIN ".center(76) + "║" + C.RESET)
    print(C.CYAN + C.BOLD + "║" + " HỆ THỐNG CHẤM ĐIỂM TỰ ĐỘNG - MÔN THI: LẬP TRÌNH PYTHON ".center(76) + "║" + C.RESET)
    print(C.CYAN + C.BOLD + "║" + " CA THI: 9H45 | MÃ ĐỀ: 11301 | THANG ĐIỂM: 10.0 ".center(76) + "║" + C.RESET)
    print(C.CYAN + C.BOLD + "╚" + "═" * 76 + "╝" + C.RESET)

def lay_thong_tin_sinh_vien():
    print(C.YELLOW + C.BOLD + "\n📋 THÔNG TIN THÍ SINH DỰ THI:" + C.RESET)
    try:
        hoten = input(C.WHITE + "   👉 Nhập Họ và Tên sinh viên (Enter để bỏ qua): " + C.RESET).strip()
        if not hoten: hoten = "Sinh Viên Chưa Đặt Tên"
        mssv = input(C.WHITE + "   👉 Nhập Mã số sinh viên (MSSV): " + C.RESET).strip()
        if not mssv: mssv = "MSSV_CHUA_CO"
        lop = input(C.WHITE + "   👉 Nhập Lớp / Khóa học: " + C.RESET).strip()
        if not lop: lop = "Lớp Python"
    except Exception:
        hoten, mssv, lop = "Sinh Viên", "MSSV", "CNTT"
    return hoten, mssv, lop

def xep_loai(diem):
    if diem >= 9.0: return "XUẤT SẮC (A+)", C.GREEN
    if diem >= 8.0: return "GIỎI (A)", C.GREEN
    if diem >= 6.5: return "KHÁ (B)", C.CYAN
    if diem >= 5.0: return "TRUNG BÌNH (C)", C.YELLOW
    return "CHƯA ĐẠT / CẦN ÔN LẠI (D/F)", C.RED

def ve_thanh_tien_trinh(diem, max_diem=10.0, do_dai=30):
    ty_le = min(max(diem / max_diem, 0.0), 1.0)
    so_o = int(ty_le * do_dai)
    thanh = "█" * so_o + "░" * (do_dai - so_o)
    pt = ty_le * 100
    return f"[{thanh}] {pt:.1f}%"

def xuat_file_ket_qua(hoten, mssv, lop, results, tong_diem):
    ten_file = "PHIEU_DIEM_DE1.txt"
    filepath = os.path.join(DIR_PATH, ten_file)
    now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    xep_loai_str, _ = xep_loai(tong_diem)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("=" * 80 + "\n")
        f.write("      PHIẾU ĐÁNH GIÁ KẾT QUẢ THI MÔN LẬP TRÌNH PYTHON - ĐỀ 1 (9H45)\n")
        f.write("=" * 80 + "\n")
        f.write(f" Họ và tên thí sinh : {hoten}\n")
        f.write(f" Mã số sinh viên    : {mssv}\n")
        f.write(f" Lớp học            : {lop}\n")
        f.write(f" Ngày giờ chấm thi  : {now}\n")
        f.write("-" * 80 + "\n")
        f.write(f"{'CÂU':<8} | {'FILE':<12} | {'ĐIỂM ĐẠT':<10} | {'ĐIỂM TỐI ĐA':<12} | GHI CHÚ ĐÁNH GIÁ\n")
        f.write("-" * 80 + "\n")
        for cau, fname, max_s, s, msg in results:
            status = "PASS" if s == max_s else ("PARTIAL" if s > 0 else "FAIL")
            f.write(f"{cau:<8} | {fname:<12} | {s:<10.2f} | {max_s:<12.2f} | [{status}] {msg}\n")
        f.write("=" * 80 + "\n")
        f.write(f"👉 TỔNG ĐIỂM: {tong_diem:.2f} / 10.0 ĐIỂM\n")
        f.write(f"👉 XẾP LOẠI : {xep_loai_str}\n")
        f.write("=" * 80 + "\n")
    return ten_file

def main():
    in_header()
    hoten, mssv, lop = lay_thong_tin_sinh_vien()

    print(C.CYAN + "\n" + "─" * 78 + C.RESET)
    print(C.BOLD + "🚀 BẮT ĐẦU CHẤM TỰ ĐỘNG TỪNG CÂU HỎI:" + C.RESET)
    print(C.CYAN + "─" * 78 + C.RESET)

    results = []
    tong_diem = 0.0

    for cau, fname, max_s, func in DANH_SACH_BAI:
        s, msg = func()
        tong_diem += s
        results.append((cau, fname, max_s, s, msg))

        if s == max_s:
            icon = C.GREEN + "✅ PASS   " + C.RESET
            score_str = C.GREEN + f"{s:4.2f}/{max_s:4.2f}" + C.RESET
        elif s > 0:
            icon = C.YELLOW + "⚠️ PARTIAL" + C.RESET
            score_str = C.YELLOW + f"{s:4.2f}/{max_s:4.2f}" + C.RESET
        else:
            icon = C.RED + "❌ FAIL   " + C.RESET
            score_str = C.RED + f"{s:4.2f}/{max_s:4.2f}" + C.RESET

        print(f" {icon} | {C.BOLD}{cau:<7}{C.RESET} | {fname:<10} | {score_str}đ | {msg}")

    # Bảng tổng kết
    print(C.CYAN + "\n" + "═" * 78 + C.RESET)
    print(C.BOLD + C.WHITE + "                      📊 BẢNG TỔNG HỢP KẾT QUẢ THI" + C.RESET)
    print(C.CYAN + "═" * 78 + C.RESET)
    print(f" 👤 Thí sinh : {C.BOLD}{hoten}{C.RESET} | MSSV: {C.BOLD}{mssv}{C.RESET} | Lớp: {C.BOLD}{lop}{C.RESET}")
    print(f" 🕒 Thời gian: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print(C.CYAN + "─" * 78 + C.RESET)

    xl_text, xl_color = xep_loai(tong_diem)
    progress = ve_thanh_tien_trinh(tong_diem, 10.0)

    print(f" 🎯 Tiến trình hoàn thành : {C.CYAN}{progress}{C.RESET}")
    print(f" 🏆 TỔNG ĐIỂM ĐẠT ĐƯỢC    : {xl_color}{C.BOLD}{tong_diem:.2f} / 10.0 ĐIỂM{C.RESET}")
    print(f" 🎖️ XẾP LOẠI NĂNG LỰC     : {xl_color}{C.BOLD}{xl_text}{C.RESET}")
    print(C.CYAN + "═" * 78 + C.RESET)

    # Xuất file kết quả
    ten_file = xuat_file_ket_qua(hoten, mssv, lop, results, tong_diem)
    print(C.GREEN + f" 💾 Đã lưu kết quả chi tiết ra phiếu điểm: {C.BOLD}{ten_file}{C.RESET}")
    print(C.CYAN + "═" * 78 + "\n" + C.RESET)

if __name__ == "__main__":
    main()
