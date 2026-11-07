# Câu 1b (0.75 điểm): Viết hàm con tính tổng tất cả các ước số của n

n = int(input("Nhập số nguyên dương n: "))

def TongUocSo(n):
    tong = 0
    for i in range(1, n + 1):
        if n % i == 0:
            tong += i
    return tong

print("Tổng các ước số là: ", TongUocSo(n))
