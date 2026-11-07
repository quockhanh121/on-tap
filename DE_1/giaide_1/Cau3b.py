# Câu 3b (0.75 điểm): In ra màn hình các số dương chẵn có trong danh sách

list_so = []
while True:
    x = int(input("Nhập phần tử (dừng khi nhập 0): "))
    if x == 0:
        break
    list_so.append(x)

DuongChan = []
for i in list_so:
    if (i > 0) and (i % 2 == 0):
        DuongChan.append(i)

if DuongChan:
    print("Các số dương chẵn có trong danh sách: ", DuongChan)
else:
    print("Không có số dương chẵn trong danh sách.")
