# Câu 1a (0.5 điểm): Kiểm tra giá trị n nếu ngoài đoạn [1;1500] thì yêu cầu nhập lại

n = int(input("Nhập giá trị 1<=n<=1500: "))
while n < 1 or n > 1500:
    n = int(input("Nhập lại giá trị 1<=n<=1500: "))

print("Giá trị n hợp lệ vừa nhập là:", n)

