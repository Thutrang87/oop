from abc import ABC, abstractmethod
class GiaKhongHopLe(Exception):
    def __init__(self, gia):
        super().__init__(f"Giá không hợp lệ: {gia}. Giá phải >=0.")
class MaHangTrungLap(Exception):
    def __init__(self, ma_hang):
        super().__init__(f"Mã hàng '{ma_hang}' đã tồn tại trong danh sách.")
class HangHoa(ABC):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia):
        self.__ma_hang = ma_hang
        self.__ten_hang = ten_hang
        self.__nha_sx = nha_sx
        self.__gia = gia
    @property
    def ma_hang(self):
        return self.__ma_hang
    @property
    def ten_hang(self):
        return self.__ten_hang 
    @property
    def nha_sx(self):
        return self.__nha_sx
    @property
    def gia(self):
        return self.__gia
    @gia.setter
    def gia(self, value):
        if value < 0:
            raise GiaKhongHopLe(value)
        self.__gia = value
    @abstractmethod
    def loai_hang(self) -> str:
        """Trả về tên loại hàng"""
        pass
    @abstractmethod
    def in_ttin(self):
        """In thông tin chi tiết của hàng hóa"""
        pass
    def __str__(self):
        return (f"[{self.loai_hang()}] {self.ma_hang} - {self.ten_hang} | Nhà SX: {self.nha_sx} | Giá: {self.gia:,.0f} VND")
    def __eq__(self, other):
        if not isinstance(other, HangHoa):
            return NotImplemented
        return self.ma_hang == other.ma_hang
    def __lt__(self, other):
        if not isinstance(other, HangHoa):
            return NotImplemented
        return self.gia < other.gia
    def __hash__(self):
        return hash(self.ma_hang)
class HangDienMay(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia,tg_bao_hanh,dien_ap, cong_suat):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.__cong_suat = cong_suat
        self.__tg_bao_hanh = tg_bao_hanh
        self.__dien_ap = dien_ap
    def loai_hang(self) -> str:
        return "Điện Máy"
    def in_ttin(self):
        print(self)
        print(f"Bảo hành: {self.__tg_bao_hanh} tháng")
        print(f"Điện áp: {self.__dien_ap} V")
        print(f"Công suất: {self.__cong_suat} W")
class HangSanhSu(HangHoa):
        def __init__(self, ma_hang, ten_hang, nha_sx, gia, loai_nguyen_lieu):
            super().__init__(ma_hang, ten_hang, nha_sx, gia)
            self.__loai_nguyen_lieu = loai_nguyen_lieu
        def loai_hang(self) -> str:
            return "Sành Sứ"
        def in_ttin(self):
            print(self)
            print(f"Loại nguyên liệu: {self.__loai_nguyen_lieu}")
class HangThucPham(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, ngay_sx, ngay_het_han):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.__ngay_sx = ngay_sx
        self.__ngay_het_han = ngay_het_han
    def loai_hang(self) -> str:
        return "Thực Phẩm"
    def in_ttin(self):
        print(self)
        print(f"Ngày sản xuất: {self.__ngay_sx}")
        print(f"Ngày hết hạn: {self.__ngay_het_han}")

class QuanLyHangHoa:
    def __init__(self):
        self.__danh_sach_hang = []
    def them_hang(self, hang: HangHoa):
        """Thêm hàng, raise MaHangTrungLap nếu mã hàng đã tồn tại"""
        if hang in self.__danh_sach_hang:
            raise MaHangTrungLap(hang.ma_hang)  
        self.__danh_sach_hang.append(hang)
    def in_tat_ca(self):
        """In thông tin tất cả hàng hóa"""
        print("=" * 40)
        print(f"DANH SÁCH HÀNG HÓA {len(self.__danh_sach_hang)} MẶT HÀNG")
        print("=" * 40)
        for sp in self.__danh_sach_hang:
            sp.in_ttin()
            print("-" * 40)
    def sap_xep_theo_gia(self):
        """Sắp xếp tăng dần theo giá"""
        return sorted(self.__danh_sach_hang)
    def tap_hop_ma_hang(self):
        """Trả về tập hợp mã hàng để kiểm tra trùng lặp"""
        return {sp.ma_hang for sp in self.__danh_sach_hang}
    def luu_file(self, filename):
        """Lưu danh sách hàng hóa vào file (định dạng CSV)"""
        with open (filename, 'w', encoding='utf-8') as f:
            for sp in self.__danh_sach_hang:
                f.write(str(sp) + '\n')
    def doc_file(self, filename):
        """Đọc và in nội dung file — Context Manager (with open)."""
        print(f"\n Nội dung file '{filename}':")
        with open(filename, "r", encoding="utf-8") as f:
            for dong in f:
                print(" ", dong.strip())
                
if __name__ == "__main__":
    ql = QuanLyHangHoa()
    ql.them_hang(HangDienMay("DM001", "Tivi Samsung 55 inch", "Samsung", 15000000, 24, 220, 150))
    ql.them_hang(HangDienMay("DM002", "Tủ lạnh LG 300L", "LG", 12000000, 36, 220, 200))
    ql.them_hang(HangSanhSu("SS001", "Bộ bát đĩa cao cấp", "Minh Long", 1_200_000, "Sứ xương cao cấp"))
    ql.them_hang(HangSanhSu("SS002", "Bộ ấm chén sứ trắng", "Bát Tràng", 500000, "Sứ trắng cao cấp"))
    ql.them_hang(HangThucPham("TP001", "Gạo ST25", "Vinafood", 200000, "2024-01-01", "2025-01-01"))
    ql.them_hang(HangThucPham("TP002","Sữa tươi Vinamilk",  "Vinamilk",     35_000, "01/07/2025", "01/08/2025"))
    ql.in_tat_ca()
    print("\n Sắp xếp theo giá tăng dần:")
    for sp in ql.sap_xep_theo_gia():
        print(f" {sp.gia:>12,.0f} VND - {sp.ten_hang} ({sp.ma_hang})")
    print(f"\n Tập hợp mã hàng: {ql.tap_hop_ma_hang()}")
    ql.luu_file("hang_hoa.txt")
    ql.doc_file("hang_hoa.txt")
    print("\n Demo Custom Exception:")
    try:
        ql.them_hang(HangSanhSu("SS001", "Lọ hoa", "Bát Tràng", 200_000, "Gốm"))
    except MaHangTrungLap as e:
        print(f"  Lỗi MaHangTrungLap: {e}")
    try:
        HangDienMay("DM999", "Quạt lỗi", "ABC", 500, 12, "220V", 50)
    except GiaKhongHopLe as e:
        print(f"  Lỗi MaHangTrungLap: {e}")
        
