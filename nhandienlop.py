# =========== LỚP CON CHÓ ===========
class ConCho:
    def __init__(self, ten, mau_sac, giong, cam_xuc):
        self.ten = ten
        self.mau_sac = mau_sac
        self.giong = giong
        self.cam_xuc = cam_xuc
    def sua (self):
        print(f"{self.ten} đang sủa: Gâu gâu!")
    def vay_duoi (self):
        print(f"{self.ten} đang vẫy đuôi vui mừng!")
    def an (self):
        print(f"{self.ten} đang ăn ngon lành!")
    def chay (self):
        print(f"{self.ten} đang chạy nhanh!")
    def gioi_thieu (self):
        print(f" Tên: {self.ten} | Màu: {self.mau_sac} | Giống: {self.giong} | Cảm xúc: {self.cam_xuc}")

# =========== LỚP Ô TÔ ===========
class OTo:
    def __init__(self, hang, kich_thuoc, mau_sac, gia):
        self.hang = hang
        self.kich_thuoc = kich_thuoc
        self.mau_sac = mau_sac
        self.gia = gia
    def tang_toc(self):
        print(f"Xe {self.hang} đang tăng tốc! Vroom!")
    def giam_toc(self):
        print(f"Xe {self.hang} đang giảm tốc...")
    def dam(self):
        print(f"Xe {self.hang} bị đâm! Bùm!")
    def gioi_thieu(self):
        print(f" Hãng: {self.hang} | Kích thước: {self.kich_thuoc} | Màu sắc: {self.mau_sac} | Giá: {self.gia}")

# =========== LỚP TÀI KHOẢN ===========
class TaiKhoan:
    def __init__(self, ten_tk, so_tk, ngan_hang, so_du):
        self.ten_tk = ten_tk
        self.so_tk = so_tk
        self.ngan_hang = ngan_hang
        self.so_du = so_du
    def rut(self, so_tien):
        if so_tien > self.so_du:
            print(f"Số dư không đủ! Hiện có: {self.so_du:,} VND")
        else:
            self.so_du -= so_tien
            print(f"Rút {so_tien:,} VND. Số dư còn: {self.so_du:,} VND")
    def gui(self, so_tien):
        self.so_du += so_tien
        print(f"Gửi {so_tien:,} VND. Số dư mới: {self.so_du:,} VND")
    def kiem_tra_so_du(self):
        print(f"Số dư tài khoản {self.so_tk}: {self.so_du:,} VND")
    def gioi_thieu(self):
        print(f" Tên TK: {self.ten_tk} | Số TK: {self.so_tk} | Ngân hàng: {self.ngan_hang}")

cho = ConCho("Milu", "vàng", "Corgi", "vui vẻ")
cho.gioi_thieu()
cho.sua()
cho.vay_duoi()
cho.an()
cho.chay()

xe = OTo("Toyota", "trung bình", "trắng", 800_000_000)
xe.gioi_thieu()
xe.tang_toc()
xe.giam_toc()

tk = TaiKhoan("Nguyen Van An", "123456789", "Techcombank", 7_000_000)
tk.gioi_thieu()
tk.gui(5_000_000)
tk.rut(3_500_000)
tk.kiem_tra_so_du()
