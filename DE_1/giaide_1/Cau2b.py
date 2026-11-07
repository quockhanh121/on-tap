# Câu 2b (0.5 điểm): Kiểm tra xem chuỗi s có đối xứng hay không?

s = input("Nhập chuỗi s: ")

def DoiXung(s):
    if s == s[::-1]:
        print("Chuỗi đối xứng.")
    else:
        print("Chuỗi không đối xứng.")

DoiXung(s)
