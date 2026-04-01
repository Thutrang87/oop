LUONG_CO_BAN = 5_000_000
class NhanVien:
    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da):
        self._ma_nv = ma_nv
        self._ho_ten = ho_ten
        self._nam_sinh = nam_sinh
        self._gioi_tinh = gioi_tinh
        self._dia_chi = dia_chi
        self._he_so_luong = he_so_luong
        self._luong_toi_da = luong_toi_da
    def tinh_luong(self):
        return LUONG_CO_BAN * self._he_so_luong
    def hien_thi(self):
        print(f"Mã NV: {self._ma_nv}")
        print(f"Họ và tên: {self._ho_ten}")
        print(f"Năm sinh: {self._nam_sinh}")
        print(f"Giới tính: {self._gioi_tinh}")
        print(f"Địa chỉ: {self._dia_chi}")
        print(f"Hệ số lương: {self._he_so_luong}")
        print(f"Lương: {self._luong_toi_da}")
class CongTacVien(NhanVien):
    HD_HOP_LE = ["3 tháng", "6 tháng", "1 năm"]
    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da, thoi_han_hd, phu_cap_ld):
        super().__init__(ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da)
        if thoi_han_hd not in CongTacVien.HD_HOP_LE:
            raise ValueError(f"Thời hạn hợp đồng phải là: {', '.join(CongTacVien.HD_HOP_LE)}")
        self._thoi_han_hd = thoi_han_hd
        self._phu_cap_ld = phu_cap_ld
    def tinh_luong(self):
        return super().tinh_luong() + self._phu_cap_ld
    def hien_thi(self):
        print("=== Cộng tác viên ===")
        super().hien_thi()
        print(f"Thời hạn hợp đồng: {self._thoi_han_hd}")
        print(f"Phụ cấp lao động: {self._phu_cap_ld:,.0f} VND")
class NVChinhThuc(NhanVien):
    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da, vi_tri):
        super().__init__(ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da)
        self._vi_tri = vi_tri
    def hien_thi(self):
        print("=== Nhân viên chính thức ===")
        super().hien_thi()
        print(f"Vị trí: {self._vi_tri}")
class TruongPhong(NhanVien):
    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da, ngay_bat_dau_ql, phu_cap_ql):
        super().__init__(ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da)
        self._ngay_bat_dau_ql = ngay_bat_dau_ql
        self._phu_cap_ql = phu_cap_ql
    def tinh_luong(self):
        return super().tinh_luong() + self._phu_cap_ql
    def hien_thi(self):
        print("=== Trưởng phòng ===")
        super().hien_thi()
        print(f"Ngày bắt đầu quản lý: {self._ngay_bat_dau_ql}")
        print(f"Phụ cấp quản lý: {self._phu_cap_ql:,.0f} VND")
      
ctv = CongTacVien("CTV001", "Nguyen Van A", 1990, "Nam", "Ha Noi", 1.5, 7_500_000, "6 tháng", 1_000_000)
nv = NVChinhThuc("NV001", "Tran Thi B", 1985, "Nu", "Da Nang", 2.0, 10_000_000, "Nhan vien kinh doanh")
tp = TruongPhong("TP001", "Le Van C", 1980, "Nam", "Ho Chi Minh", 3.0, 15_000_000, "01/01/2020", 5_000_000)
ctv.hien_thi()
print()
nv.hien_thi()
print()
tp.hien_thi()
print("\n ===== BẢNG TÍNH LƯƠNG PHÒNG BAN =====")
ds_nv = [ctv, nv, tp]
for nv in ds_nv:
    print(f"{nv._ho_ten}: {nv.tinh_luong():,.0f} VND")
