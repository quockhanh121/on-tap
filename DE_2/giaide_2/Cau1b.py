# Câu 1b (0.75 điểm): Viết hàm con đếm số lượng chữ số lẻ của số nguyên dương n

n = int(input("Nhập số nguyên dương n: "))

def DemChuSoLe(n):
    dem = 0
    while n != 0:
        tam = n % 10
        if tam % 2 != 0:
            dem += 1
        n //= 10
    return dem

print("Số lượng chữ số lẻ là: ", DemChuSoLe(n))

