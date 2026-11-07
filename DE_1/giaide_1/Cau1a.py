# Câu 1a (0.5 điểm): Kiểm tra giá trị n nếu ngoài đoạn [1;99] thì yêu cầu nhập lại

n = int(input("Nhập giá trị n:"))
while n<=1 or n>=99:
    n = int(input("Yêu cầu nhập lại n:"))
print("n=",n)





