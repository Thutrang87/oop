class NhanVien:
    LUONG_MAX = 100_000_000  
    def __init__(self, ten_nhan_vien: str, luong_co_ban: float, he_so_luong: float):
        self.__ten_nhan_vien = ten_nhan_vien
        self.__luong_co_ban = luong_co_ban
        self.__he_so_luong = he_so_luong
    def get_ten_nhan_vien(self):
        return self.__ten_nhan_vien
    def set_ten_nhan_vien(self, ten):
        self.__ten_nhan_vien = ten
    def get_luong_co_ban(self):
        return self.__luong_co_ban
    def set_luong_co_ban(self, luong):
        if luong >= 0:
            self.__luong_co_ban = luong
        else:
            print("Lương cơ bản không được âm!")
    def get_he_so_luong(self):
        return self.__he_so_luong
    def set_he_so_luong(self, he_so):
        if he_so >= 0:
            self.__he_so_luong = he_so
        else:
            print("Hệ số lương không được âm!")
    def tinhLuong(self) -> float:
        return self.__luong_co_ban * self.__he_so_luong
    def inTTin(self):
        print(f"Tên nhân viên : {self.__ten_nhan_vien}")
        print(f"Lương cơ bản  : {self.__luong_co_ban:,.0f} VND")
        print(f"Hệ số lương   : {self.__he_so_luong}")
        print(f"Lương thực tế : {self.tinhLuong():,.0f} VND")
    def tangLuong(self, delta: float) -> bool:
        luong_moi = self.tinhLuong() + delta
        if luong_moi > NhanVien.LUONG_MAX:
            print(f"Không thể tăng! Lương mới {luong_moi:,.0f} > LUONG_MAX {NhanVien.LUONG_MAX:,.0f}")
            return False
        else:
            self.__luong_co_ban += delta / self.__he_so_luong
            print(f"Tăng lương thành công! Lương mới: {self.tinhLuong():,.0f} VND")
            return True

nv1 = NhanVien("Nguyễn Văn A", 10_000_000, 3.5)
nv1.inTTin()

print("\n--- Tăng lương 5 triệu ---")
nv1.tangLuong(5_000_000)
nv1.inTTin()

print("\n--- Tăng lương vượt mức tối đa ---")
nv1.tangLuong(500_000_000)

print("\n--- Test getter/setter ---")
nv1.set_ten_nhan_vien("Trần Thị B")
nv1.set_luong_co_ban(15_000_000)
print(f"Tên mới: {nv1.get_ten_nhan_vien()}")
print(f"Lương cơ bản mới: {nv1.get_luong_co_ban():,.0f} VND")
