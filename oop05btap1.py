class HangHoa:
    def __init__(self, ma_hang, ten_hang, nha_sx, gia):
        self._ma_hang = ma_hang
        self._ten_hang = ten_hang
        self._nha_sx = nha_sx
        self._gia = gia
    def get_ma_hang(self):
        return self._ma_hang
    def get_ten_hang(self):
        return self._ten_hang
    def get_nha_sx(self):
        return self._nha_sx
    def get_gia(self):
        return self._gia
    def hien_thi(self):
        print(f"Ma hang: {self._ma_hang} | Ten hang: {self._ten_hang} | Nha san xuat: {self._nha_sx} | Gia: {self._gia:,.0f} VND")
class HangDienHoa(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, tg_bao_hanh, dien_ap, cong_suat):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self._tg_bao_hanh = tg_bao_hanh
        self._dien_ap = dien_ap
        self._cong_suat = cong_suat
    def hien_thi(self):
        print("=== Hàng Điện Máy ===")  
        super().hien_thi()
        print(f"Bảo hành: {self._tg_bao_hanh} tháng | Điện áp: {self._dien_ap} | Công suất: {self._cong_suat:.0f} W")
class HangSanhSu(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, loai_nguyen_lieu):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self._loai_nguyen_lieu = loai_nguyen_lieu
    def hien_thi(self):
        print("=== Hàng Sành Sứ ===")  
        super().hien_thi()
        print(f"Nguyên liệu: {self._loai_nguyen_lieu}")
class HangThucPham(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, ngay_sx, ngay_het_han):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self._ngay_sx = ngay_sx
        self._ngay_het_han = ngay_het_han
    def hien_thi(self):
        print("=== Hàng Thực Phẩm ===")  
        super().hien_thi()
        print(f"Ngày sản xuất: {self._ngay_sx} | Ngày hết hạn: {self._ngay_het_han}")

dm = HangDienHoa("DH001", "Tivi Samsung", "Samsung", 15000000, 24, "220V", 100)
ss = HangSanhSu("SS001", "Bộ ấm chén", "Bát Tràng", 500000, "Sứ cao cấp")
tp = HangThucPham("TP001", "Gạo ST25", "An Giang", 200000, "01/01/2024", "01/01/2025")
dm.hien_thi()
print()
ss.hien_thi()
print()
tp.hien_thi()
