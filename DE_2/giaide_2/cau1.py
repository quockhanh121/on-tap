# Câu 1 (2.0 điểm)

# a. Kiểm tra giá trị n nếu ngoài đoạn [1;1500] thì yêu cầu nhập lại (0.5 điểm)
n = int(input("Nhập giá trị 1<=n<=1500: "))
while n < 1 or n > 1500:
    n = int(input("Nhập lại giá trị 1<=n<=1500: "))

# b. Viết hàm con đếm số lượng chữ số lẻ của số nguyên dương n (0.75 điểm)
def DemChuSoLe(n):
    dem = 0
    while n != 0:
        tam = n % 10
        if tam % 2 != 0:
            dem += 1
        n //= 10
    return dem

print("Số lượng chữ số lẻ là:", DemChuSoLe(n))

# c. Viết hàm con tính S = 1/2 + 1/4 + 1/6 + ... + 1/(2n) (0.75 điểm)
def S(n):
    s = 0
    for i in range(1, n + 1):
        s += 1 / (2 * i)
    return s

print("S =", S(n))

