# -*- coding: utf-8 -*-
"""
BỘ TEST CHẤM ĐIỂM TỰ ĐỘNG - 13 FILE RIÊNG BIỆT (ĐỀ 2 - MÃ ĐỀ: 11301)
Thang điểm chuẩn: 10.0 điểm
Tự động tìm file trong thư mục hiện tại hoặc các thư mục con (giaide_2,...)
"""

import sys
import subprocess
import os

# Cấu hình encoding UTF-8 cho console Windows
if sys.platform == "win32":
    try:
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    except Exception:
        pass

DIR_PATH = os.path.dirname(os.path.abspath(__file__))

def find_file(filename):
    """Tìm file trong thư mục hiện tại hoặc các thư mục con (như giaide_2)"""
    direct_path = os.path.join(DIR_PATH, filename)
    if os.path.exists(direct_path):
        return direct_path
    for root, dirs, files in os.walk(DIR_PATH):
        if filename in files:
            return os.path.join(root, filename)
    return None

def run_script(filename, input_data="", timeout=3):
    filepath = find_file(filename)
    if not filepath or not os.path.exists(filepath):
        return None, "", f"File {filename} không tồn tại (đã quét cả các thư mục con)"
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
        return -1, "", "Hết thời gian chờ (Có thể bị lặp vô tận while/for)"
    except Exception as e:
        return -2, "", str(e)


def test_Cau1a():
    ret, out, err = run_script("Cau1a.py", input_data="-5\n2000\n635\n")
    if ret == 0 and ("nhập lại" in out.lower() or out.lower().count("nhập") >= 3) and "635" in out:
        return 0.5, "✅ Cau1a.py (0.5/0.5đ): Kiểm tra và yêu cầu nhập lại khi n ngoài [1;1500] thành công."
    elif ret == 0:
        return 0.25, f"⚠️ Cau1a.py (0.25/0.5đ): Có chạy được nhưng chưa thấy thông báo nhập lại rõ ràng. Output: {out.strip()}"
    return 0.0, f"❌ Cau1a.py (0.0/0.5đ): Lỗi chạy file: {err or out}"


def test_Cau1b():
    ret, out, err = run_script("Cau1b.py", input_data="635\n")
    if ret == 0 and ("2" in out and "lẻ" in out.lower()):
        return 0.75, "✅ Cau1b.py (0.75/0.75đ): Hàm DemChuSoLe(635) trả về 2 chữ số lẻ chính xác."
    elif ret == 0 and "2" in out:
        return 0.5, f"⚠️ Cau1b.py (0.5/0.75đ): Có kết quả 2 nhưng định dạng in chưa khớp. Output: {out.strip()}"
    return 0.0, f"❌ Cau1b.py (0.0/0.75đ): Lỗi chạy file: {err or out}"


def test_Cau1c():
    ret, out, err = run_script("Cau1c.py", input_data="2\n")
    if ret == 0 and ("0.75" in out or "3/4" in out):
        return 0.75, "✅ Cau1c.py (0.75/0.75đ): Hàm S(2) tính ra 0.75 (1/2 + 1/4) chính xác."
    elif ret == 0 and ("s =" in out.lower() or "s=" in out.lower()):
        return 0.5, f"⚠️ Cau1c.py (0.5/0.75đ): Có tính S nhưng kết quả với n=2 chưa ra 0.75. Output: {out.strip()}"
    return 0.0, f"❌ Cau1c.py (0.0/0.75đ): Lỗi chạy file: {err or out}"


def test_Cau2a():
    ret, out, err = run_script("Cau2a.py", input_data="Python Pro\n")
    if ret == 0 and "2" in out:
        return 0.75, "✅ Cau2a.py (0.75/0.75đ): Đếm số ký tự chữ hoa chính xác ('Python Pro' -> 2)."
    ret2, out2, err2 = run_script("Cau2a.py", input_data="abc\n")
    if ret2 == 0 and ("không có ký tự chữ hoa" in out2.lower() or "0" in out2):
        return 0.5, "⚠️ Cau2a.py (0.5/0.75đ): Nhận diện đúng khi không có chữ hoa nhưng đếm số lượng chưa chuẩn."
    return 0.0, f"❌ Cau2a.py (0.0/0.75đ): Lỗi chạy file: {err or out}"


def test_Cau2b():
    ret, out, err = run_script("Cau2b.py", input_data="radar\n")
    ret_no, out_no, err_no = run_script("Cau2b.py", input_data="python\n")
    if ret == 0 and ret_no == 0 and "chuỗi đối xứng" in out.lower() and "chuỗi không đối xứng" in out_no.lower():
        return 0.5, "✅ Cau2b.py (0.5/0.5đ): Hàm DoiXung(s) nhận diện cả đối xứng và không đối xứng chính xác."
    elif ret == 0 and "đối xứng" in out.lower():
        return 0.25, "⚠️ Cau2b.py (0.25/0.5đ): Đã in chuỗi đối xứng nhưng chưa kiểm tra trường hợp không đối xứng."
    return 0.0, f"❌ Cau2b.py (0.0/0.5đ): Lỗi chạy file: {err or out}"


def test_Cau2c():
    ret, out, err = run_script("Cau2c.py", input_data="abc123d4\n")
    if ret == 0 and "10" in out:
        return 0.75, "✅ Cau2c.py (0.75/0.75đ): Tính tổng các chữ số chính xác ('abc123d4' -> 10)."
    return 0.0, f"❌ Cau2c.py (0.0/0.75đ): Lỗi chạy file: {err or out}"


def test_Cau3a():
    ret, out, err = run_script("Cau3a.py", input_data="10\n-5\n8\n0\n")
    if ret == 0 and "[" in out and "]" in out and "10" in out and "-5" in out and "8" in out:
        return 0.75, "✅ Cau3a.py (0.75/0.75đ): Nhập danh sách dừng khi gặp 0 và in đúng [10, -5, 8]."
    elif ret == 0 and "[" in out:
        return 0.5, f"⚠️ Cau3a.py (0.5/0.75đ): Có in danh sách nhưng thiếu phần tử. Output: {out.strip()}"
    return 0.0, f"❌ Cau3a.py (0.0/0.75đ): Lỗi chạy file: {err or out}"


def test_Cau3b():
    ret, out, err = run_script("Cau3b.py", input_data="2\n-4\n6\n7\n0\n")
    if ret == 0 and "8" in out and ("tổng" in out.lower() or "dương chẵn" in out.lower()):
        return 0.75, "✅ Cau3b.py (0.75/0.75đ): Tính tổng các số dương chẵn chính xác (2 + 6 = 8)."
    elif ret == 0 and "8" in out:
        return 0.5, f"⚠️ Cau3b.py (0.5/0.75đ): Có ra số 8 nhưng chưa in rõ định dạng."
    return 0.0, f"❌ Cau3b.py (0.0/0.75đ): Lỗi chạy file: {err or out}"


def test_Cau3c():
    ret, out, err = run_script("Cau3c.py", input_data="5\n2\n5\n5\n0\n5\n")
    if ret == 0 and ("3" in out and ("lần" in out.lower() or "xuất hiện" in out.lower())):
        return 0.5, "✅ Cau3c.py (0.5/0.5đ): Đếm số lần xuất hiện của k chính xác (k=5 -> 3 lần)."
    return 0.0, f"❌ Cau3c.py (0.0/0.5đ): Lỗi chạy file: {err or out}"


def test_Cau4a():
    input_str = "1\nMS01\nLap Trinh Python\nNguyen Van A\nNXB Tre\n2022\n"
    ret, out, err = run_script("Cau4a.py", input_data=input_str)
    if ret == 0 and "{" in out and "}" in out and "MS01" in out and ("Lap Trinh Python" in out or "2022" in out):
        return 1.5, "✅ Cau4a.py (1.5/1.5đ): Nhập và lưu thông tin sách vào từ điển hoàn chỉnh."
    elif ret == 0 and "{" in out:
        return 1.0, f"⚠️ Cau4a.py (1.0/1.5đ): Có in từ điển nhưng thông tin chưa đầy đủ. Output: {out.strip()}"
    return 0.0, f"❌ Cau4a.py (0.0/1.5đ): Lỗi chạy file: {err or out}"


def test_Cau4b():
    input_str = "1\nMS01\nLap Trinh Python\nNguyen Van A\nNXB Tre\n2022\nMS01\n"
    ret, out, err = run_script("Cau4b.py", input_data=input_str)
    if ret == 0 and ("đã được xóa" in out.lower() or "xóa" in out.lower()):
        return 0.5, "✅ Cau4b.py (0.5/0.5đ): Tìm và xóa cuốn sách theo mã số thành công."
    return 0.0, f"❌ Cau4b.py (0.0/0.5đ): Lỗi chạy file: {err or out}"


def test_Cau5a():
    filepath = find_file("Cau5a.py")
    if not filepath or not os.path.exists(filepath):
        return 0.0, "❌ Cau5a.py: File không tồn tại."
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            code = f.read()
        if "class DienThoai" in code and "def __init__" in code and "thongtindienthoai" in code:
            return 1.0, "✅ Cau5a.py (1.0/1.0đ): Khai báo lớp DienThoai, __init__ và thongtindienthoai đầy đủ."
        return 0.5, "⚠️ Cau5a.py (0.5/1.0đ): Lớp DienThoai chưa đủ các phương thức theo yêu cầu."
    except Exception as e:
        return 0.0, f"❌ Cau5a.py: Lỗi đọc file: {e}"


def test_Cau5b():
    ret, out, err = run_script("Cau5b.py", input_data="")
    if ret == 0:
        has_dt1 = "DT01" in out and ("iPhone 15 Pro" in out or "apple" in out.lower())
        has_dt2 = "DT02" in out and ("Galaxy S24 Ultra" in out or "samsung" in out.lower())
        if has_dt1 and has_dt2:
            return 1.0, "✅ Cau5b.py (1.0/1.0đ): Khởi tạo 2 đối tượng điện thoại và gọi thongtindienthoai() chính xác."
        elif has_dt1 or has_dt2:
            return 0.5, "⚠️ Cau5b.py (0.5/1.0đ): Đã in được thông tin 1 điện thoại."
    return 0.0, f"❌ Cau5b.py (0.0/1.0đ): Lỗi chạy file: {err or out}"


def main():
    print("=" * 70)
    print("   HỆ THỐNG CHẤM ĐIỂM TỰ ĐỘNG - 13 FILE RIÊNG BIỆT (ĐỀ 2 - MÃ ĐỀ: 11301)")
    print("=" * 70)

    tests = [
        ("Câu 1a", 0.5, test_Cau1a),
        ("Câu 1b", 0.75, test_Cau1b),
        ("Câu 1c", 0.75, test_Cau1c),
        ("Câu 2a", 0.75, test_Cau2a),
        ("Câu 2b", 0.5, test_Cau2b),
        ("Câu 2c", 0.75, test_Cau2c),
        ("Câu 3a", 0.75, test_Cau3a),
        ("Câu 3b", 0.75, test_Cau3b),
        ("Câu 3c", 0.5, test_Cau3c),
        ("Câu 4a", 1.5, test_Cau4a),
        ("Câu 4b", 0.5, test_Cau4b),
        ("Câu 5a", 1.0, test_Cau5a),
        ("Câu 5b", 1.0, test_Cau5b),
    ]

    tong_diem = 0.0
    tong_toi_da = 10.0

    for name, max_score, func in tests:
        s, msg = func()
        tong_diem += s
        print(f"[{s:4.2f}/{max_score:4.2f}] {msg}")

    print("\n" + "=" * 70)
    print(f"🏆 TỔNG ĐIỂM BÀI THI: {tong_diem:.2f} / {tong_toi_da:.1f} ĐIỂM")
    if tong_diem >= 9.5:
        print("🎉 XUẤT SẮC! ĐẠT ĐIỂM TỐI ĐA 10/10 THEO BAREM ĐÁP ÁN!")
    print("=" * 70)


if __name__ == "__main__":
    main()
