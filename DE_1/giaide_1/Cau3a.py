# Câu 3a (0.75 điểm): Nhập các phần tử số nguyên vào danh sách, dừng khi người dùng nhập 0. In danh sách vừa nhập

list_so = []
while True:
    x = int(input("Nhập phần tử (dừng khi nhập 0): "))
    if x == 0:
        break
    list_so.append(x)

print("Danh sách vừa nhập: ", list_so)
