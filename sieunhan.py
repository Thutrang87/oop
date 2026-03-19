#LỚP SIÊU NHÂN
class SieuNhan:
    def __init__(self, ten: str, vu_khi: str, mau_sac: str):
        self.ten = ten
        self.vu_khi = vu_khi
        self.mau_sac = mau_sac
    def __str__(self):
        return(f"Siêu nhân: {self.ten} | Vũ khí: {self.vu_khi} | Màu sắc: {self.mau_sac}")
sieu_nhan_A = SieuNhan("A", "kiếm", "đỏ")
sieu_nhan_B = SieuNhan("B", "khiên", "xanh")
print(sieu_nhan_A)
print(sieu_nhan_B)

# QUẢN LÍ DANH SÁCH SIÊU NHÂN
class SieuNhan:
    def __init__(self, ten="", vu_khi="", mau_sac="", suc_manh=0):
        self.ten = ten
        self.vu_khi = vu_khi
        self.mau_sac = mau_sac
        self.suc_manh = suc_manh
    def the_hien(self):
        print(f"Siêu nhân: {self.ten} | Vũ khí: {self.vu_khi} | Màu sắc: {self.mau_sac} | Sức mạnh: {self.suc_manh}")
danh_sach = []
print("=== NHẬP DANH SÁCH SIÊU NHÂN ===")
print("(Nhấn Enter để kết thúc)\n")

while True:
    ten = input("Tên siêu nhân: ")
    if ten == "":
        break
    vu_khi = input("Vũ khí: ")
    mau_sac = input("Màu sắc: ")
    suc_manh = input("Sức mạnh (1-100): ")
    danh_sach.append(SieuNhan(ten, vu_khi, mau_sac, suc_manh))
    print(f"  -> Đã thêm {ten}!\n")

print(f"\n=== DANH SÁCH {len(danh_sach)} SIÊU NHÂN ===")
for i, sn in enumerate(danh_sach, start=1):
    print(f"{i}. ", end="")
    sn.the_hien()
