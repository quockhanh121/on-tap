# Câu 1c (0.75 điểm): Viết hàm con tính S = 1/2 + 1/4 + 1/6 + ... + 1/(2n)

n = int(input("Nhập số nguyên dương n: "))

def S(n):
    s = 0
    for i in range(1, n + 1):
        s += 1 / (2 * i)
    return s

print("S = ", S(n))

