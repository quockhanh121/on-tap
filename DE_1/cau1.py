# Câu 1 
n = int(input("Nhập giá trị 1<=n<=99: "))
while n < 1 or n > 99:
    n = int(input("Nhập lại giá trị 1<=n<=99: "))
 
# b. Hàm tính tổng các ước số của n
def TongUocSo(n):
    tong = 0
    for i in range(1, n + 1):
        if n % i == 0:
            tong += i
    return tong
 
# c. Hàm tính S = 1 + 2^2 + 3^3 + ... + n^n
def S(n):
    s = 0
    for i in range(1, n + 1):
        s += i ** i
    return s
 
print("Tổng các ước số của", n, "là:", TongUocSo(n))
print("S =", S(n))
