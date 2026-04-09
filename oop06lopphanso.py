from math import gcd
class MauSoBangKhong(Exception):
    """Ngoại lệ khi mẫu số bằng 0."""
    def __init__(self, msg="Mẫu số không được bằng 0."):
        super().__init__(msg)
class PhanSo:
    def __init__(self, tu_so, mau_so):
        if mau_so == 0:
            raise MauSoBangKhong()
        self.__tu_so = tu_so
        self.__mau_so = mau_so
        if self.__mau_so < 0:
            self.__tu_so = -self.__tu_so
            self.__mau_so = -self.__mau_so
    @property
    def tu_so(self):
        return self.__tu_so
    @property
    def mau_so(self):
        return self.__mau_so
    @mau_so.setter
    def mau_so(self, value):
        if value == 0:
            raise MauSoBangKhong()
        self.__mau_so = value
        if self.__mau_so < 0:
            self.__tu_so = -self.__tu_so
            self.__mau_so = -self.__mau_so
    def is_toi_gian(self):
        """Kiểm tra xem phân số đã ở dạng tối giản chưa."""
        return gcd(self.__tu_so, self.__mau_so) == 1
    def toi_gian(self):
        """Trả về phân số đã được tối giản."""
        g = gcd(abs(self.__tu_so), abs(self.__mau_so))
        return PhanSo(self.__tu_so // g, self.__mau_so // g)
    def __add__(self, other):
        tu_so = self.__tu_so * other.mau_so + other.tu_so * self.__mau_so
        mau_so = self.__mau_so * other.mau_so
        return PhanSo(tu_so, mau_so).toi_gian()
    def __sub__(self, other):
        tu_so = self.__tu_so * other.mau_so - other.tu_so * self.__mau_so
        mau_so = self.__mau_so * other.mau_so
        return PhanSo(tu_so, mau_so).toi_gian()
    def __mul__(self, other):
        tu_so = self.__tu_so * other.tu_so
        mau_so = self.__mau_so * other.mau_so
        return PhanSo(tu_so, mau_so).toi_gian()
    def __truediv__(self, other):
        if other.tu_so == 0:
            raise MauSoBangKhong("Không thể chia cho phân số có tử số bằng 0.")
        tu_so = self.__tu_so * other.mau_so
        mau_so = self.__mau_so * other.tu_so
        return PhanSo(tu_so, mau_so).toi_gian()
    def __eq__(self, other):
        a = self.toi_gian()
        b = other.toi_gian()
        return a.tu_so == b.tu_so and a.mau_so == b.mau_so
    def __lt__(self, other):
        return self.__tu_so * other.mau_so < other.tu_so * self.__mau_so
    def __str__(self):
        ps = self.toi_gian()
        if ps.mau_so == 1:
            return str(ps.tu_so)
        return f"{ps.tu_so}/{ps.mau_so}"
    def __repr__(self):
        return f"PhanSo({self.__tu_so}, {self.__mau_so})"
    def __hash__(self):
        ps = self.toi_gian()
        return hash((ps.tu_so, ps.mau_so))
def nhap_phan_so():
    """Nhập một dãy phân số từ bàn phím."""
    ds = []
    n = int(input("Nhập số lượng phân số: "))
    for i in range(n):
        while True:
            try:
                tu_so = int(input(f"Phân số {i+1} - Tử số: "))
                mau_so = int(input(f"Phân số {i+1} - Mẫu số: "))
                ds.append(PhanSo(tu_so, mau_so))
                break
            except MauSoBangKhong as e:
                print(f" Loi: {e} Vui lòng nhập lại.")
    return ds
if __name__ == "__main__":
    print("=" * 40)
    print(" BÀI 3: XÂY DỰNG LỚP PHÂN SỐ ")
    print("=" * 40)
    ds_phan_so = nhap_phan_so()
    print("\n--- Dạng tối giản của các phân số ---")
    for ps in ds_phan_so:
        print(f" {repr(ps)} -> {ps}")
    print("\n--- Sắp xếp tăng dần ---")
    ds_sap_xep = sorted(ds_phan_so)
    print("  "+" < ".join(str(ps) for ps in ds_sap_xep))
    print("\n--- Loại phân số trùng giá trị (set) ---")
    tap_hop = set(ds_phan_so)
    print("  " + ", ".join(str(ps) for ps in tap_hop))
