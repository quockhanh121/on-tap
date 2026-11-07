# Câu 3c (0.5 điểm): Đếm số lần xuất hiện của phần tử k có trong danh sách (k nhập từ bàn phím)

danhsach = []
while True:
    x = int(input("Nhập phần tử (nhập 0 để dừng): "))
    if x == 0:
        break
    danhsach.append(x)

k = int(input("Nhập k: "))
dem = 0
for i in danhsach:
    if i == k:
        dem += 1

if dem == 0:
    print("Không có phần tử", k, "trong danh sách")
else:
    print(f"Số lần xuất hiện của {k} là: ", dem)

