# Câu 3c (0.5 điểm): Đếm số lần xuất hiện của phần tử k có trong danh sách (k nhập từ bàn phím)

list_so = []
while True:
    x = int(input("Nhập phần tử (dừng khi nhập 0): "))
    if x == 0:
        break
    list_so.append(x)

k = int(input("Nhập k: "))
dem = list_so.count(k)

if dem == 0:
    print(f"{k} không có trong danh sách")
else:
    print(f"{k} xuất hiện {dem} lần")

