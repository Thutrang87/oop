class NhanVien:
  LUONG_MAX = 100_000_000
  def __init__(self, ten_nhan_vien: str, luong_co_ban: float, he_so_luong: float):
    self.__ten_nhan_vien = ten_nhan_vien
    self.__luong_co_ban = luong_co_ban
    self.__he_so_luong = he_so_luong
  def get_ten_nhan_vien(self):
    return self.__ten_nhan_vien
  def set_ten_nhan_vien(self, ten: str):
    self.__ten_nhan_vien = ten
  def get_luong_co_ban(self):
    return self.__luong_co_ban
  def set_luong_co_ban(self, luong: float):
    if luong >=0:
      self.__luong_co_ban = luong
    else:
      print ("Lương cơ bản không được âm!")
  def get_he_so_luong(self):
    return self.__he_so_luong
  def set_he_so_luong(self, he_so: float):
    if he_so >=0:
      self.__he_so_luong  = he_so
    else:
      print ("Hệ số lương không được âm!")
  def tinhLuong(self) -> float:
    return self.__luong_co_ban  * self.__he_so_luong
  def inTTin(self):
    print (f"Tên nhân viên: {self.__ten_nhan_vien}")
    print (f"Lương cơ bản:  {self.__luong_co_ban:,.0f} VND")
    print (f"Hệ số lương:   {self.__he_so_luong}")
    print (f"Lương thực tế: {self.tinhLuong():,.0f} VND")
  def tangLuong(self, delta: float) -> bool:
    luong_moi = self.__luong_co_ban * (self.__he_so_luong + delta)
    if luong_moi > NhanVien.LUONG_MAX:
      print (f"Không thể tăng! Lương mới {luong_moi:,.0f} > LUONG_MAX {NhanVien.LUONG_MAX:,.0f}")
    else:
      self.__he_so_luong += delta
      print(f"Tăng hệ số lương thành công! Hệ số mới: {self.__he_so_luong}")
      print(f"Lương mới: {self.tinhLuong():,.0f} VND")
      return True
      
print("=" * 50)
nv = NhanVien("Nguyễn Văn A", 10_000_000, 3.5)
nv.inTTin()

print("\n--- Tăng hệ số lương thêm 2.0 ---")
ket_qua = nv.tangLuong(2.0)
print(f"Kết quả: {ket_qua}")

print("\n--- Tăng hệ số lương thêm 100 (vượt mức) ---")
ket_qua = nv.tangLuong(100)
print(f"Kết quả: {ket_qua}")

print("\n--- Test getter/setter ---")
nv.set_ten_nhan_vien("Trần Thị B")
nv.set_luong_co_ban(20_000_000)
nv.set_he_so_luong(4.0)
print(f"Tên    : {nv.get_ten_nhan_vien()}")
print(f"Lương CB: {nv.get_luong_co_ban():,.0f} VND")
print(f"Hệ số  : {nv.get_he_so_luong()}")
nv.inTTin()



    
      
