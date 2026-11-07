# Câu 1c (0.75 điểm): Viết hàm con tính S = 1 + 2^2 + 3^3 + ... + n^n

n = int(input("Nhập số nguyên dương n: "))

def S(n):
    s = 0
    for i in range(1, n + 1):
        s += i ** i
    return s

print("S = ", S(n))

