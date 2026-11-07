# Câu 3a (0.75 điểm): Nhập các phần tử số nguyên vào danh sách, ngưng khi người dùng nhập số 0. In danh sách vừa nhập

danhsach = []
while True:
    x = int(input("Nhập phần tử (nhập 0 để dừng): "))
    if x == 0:
        break
    danhsach.append(x)

print("Danh sách vừa nhập: ", danhsach)

