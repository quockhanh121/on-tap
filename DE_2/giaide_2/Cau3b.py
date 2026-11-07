# Câu 3b (0.75 điểm): Tính tổng các số dương chẵn có trong danh sách

danhsach = []
while True:
    x = int(input("Nhập phần tử (nhập 0 để dừng): "))
    if x == 0:
        break
    danhsach.append(x)

tong = 0
for i in danhsach:
    if (i > 0) and (i % 2 == 0):
        tong += i

if tong != 0:
    print("Tổng các số dương chẵn trong danh sách: ", tong)
else:
    print("Không có số dương chẵn trong danh sách.")

