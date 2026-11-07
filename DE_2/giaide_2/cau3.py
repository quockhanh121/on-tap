# Câu 3 (2.0 điểm)

# a. Nhập các phần tử số nguyên vào danh sách, dừng khi nhập 0 (0.75 điểm)
danhsach = []
while True:
    x = int(input("Nhập phần tử (dừng khi nhập 0): "))
    if x == 0:
        break
    danhsach.append(x)

print("Danh sách vừa nhập:", danhsach)

# b. Tính tổng các số dương chẵn có trong danh sách (0.75 điểm)
tong = 0
for i in danhsach:
    if (i > 0) and (i % 2 == 0):
        tong += i

if tong != 0:
    print("Tổng các số dương chẵn trong danh sách:", tong)
else:
    print("Không có số dương chẵn trong danh sách.")

# c. Đếm số lần xuất hiện của phần tử k có trong danh sách (0.5 điểm)
k = int(input("Nhập phần tử k cần đếm: "))
dem = 0
for i in danhsach:
    if i == k:
        dem += 1

if dem == 0:
    print("Không có phần tử", k, "trong danh sách")
else:
    print(f"Số lần xuất hiện của {k} là:", dem)

