#Yeu cau 1: 
class CanBo:
    def __init__(self, hoten, tuoi, gioitinh, diachi):
        self._hoten = hoten
        self._tuoi = tuoi
        self._gioitinh = gioitinh
        self._diachi = diachi
    def loai_cb(self):
        return "Can Bo"
    def hien_thi(self):
        print(f"{self.loai_cb()}:, {self._hoten}")
        print(f"Tuoi: {self._tuoi} | Gioi tinh: {self._gioitinh} | Dia chi: {self._diachi}")
class CongNhan(CanBo):
    def __init__(self, hoten, tuoi, gioitinh, diachi, bac):
        super().__init__(hoten, tuoi, gioitinh, diachi)
        if not (1 <= bac <= 10):
            raise ValueError("Bac phai tu 1 den 10")
        self._bac = bac
    def loai_cb(self):
        return "Cong Nhan"
    def hien_thi(self):
        super().hien_thi()
        print(f"Bac: {self._bac}")
class KySu(CanBo):
    def __init__(self, hoten, tuoi, gioitinh, diachi, nganh):
        super().__init__(hoten, tuoi, gioitinh, diachi)
        self._nganh = nganh
    def loai_cb(self):
        return "Ky Su"
    def hien_thi(self):
        super().hien_thi()
        print(f"Nganh: {self._nganh}")
class NhanVien(CanBo):
    def __init__(self, hoten, tuoi, gioitinh, diachi, congviec):
        super().__init__(hoten, tuoi, gioitinh, diachi)
        self._congviec = congviec
    def loai_cb(self):
        return "Nhan Vien"
    def hien_thi(self):
        super().hien_thi()
        print(f"Cong viec: {self._congviec}")

#Yeu cau 2:
class QLCB:
    def __init__(self):
        self.__ds_can_bo = []
        self.__ds_can_bo.append(CongNhan("Nguyen Van A", 30, "Nam", "Ha Noi", 5))
        self.__ds_can_bo.append(KySu("Tran Thi B", 28, "Nu", "Da Nang", "CNTT"))
        self.__ds_can_bo.append(NhanVien("Le Van C", 35, "Nam", "Ho Chi Minh", "Van phong"))
    def them_moi(self):
        print("/n ====== Them can bo moi ======")
        print("Chon loai can bo:")
        print("1. Cong Nhan")
        print("2. Ky Su")
        print("3. Nhan Vien")
        loai = input("Nhap lua chon (1-3): ").strip()
        ho_ten = input("Ho ten:")
        tuoi = int(input("Tuoi:"))
        gioi_tinh = input("Gioi tinh:")
        dia_chi = input("Dia chi:")
        if loai == "1":
            bac = int(input("Bac (1-10):"))
            can_bo = CongNhan(ho_ten, tuoi, gioi_tinh, dia_chi, bac)
        elif loai == "2":
            nganh = input("Nganh:")
            can_bo = KySu(ho_ten, tuoi, gioi_tinh, dia_chi, nganh)
        elif loai == "3":
            cong_viec = input("Cong viec:")
            can_bo = NhanVien(ho_ten, tuoi, gioi_tinh, dia_chi, cong_viec)
        else:
            print("Lua chon khong hop le!")
            return
        self.__ds_can_bo.append(can_bo)
        print(f"Da them: {can_bo}")
    def tim_kiem(self):
        print("/n ====== Tim kiem can bo ======")
        tu_khoa = input("Nhap ten can tim:").strip().lower()
        ket_qua = [cb for cb in self.__ds_can_bo if tu_khoa in cb._ho_ten.lower()]
        if not ket_qua:
            print("Khong tim thay can bo nao!")
        else:
            print(f"Tim thay {len(ket_qua)} ket qua:")
            for cb in ket_qua:
                print()
                cb.hien_thi()
    def hien_thi_ds(self):
        if not self.__ds_can_bo:
            print("/n Danh sach can bo trong!")
            return                     
        print(f"/n ====== DANH SACH CAN BO ({len(self.__ds_can_bo)} nguoi) ======")
        for i, cb in enumerate(self.__ds_can_bo, start=1):
            print(f"STT: {i}")
            cb.hien_thi()
    def chay_menu(self):
        while True:
            print("\n ||==============================||")
            print("   ||        QUAN LY CAN BO        ||")
            print("   ||1. Them can bo moi            ||")
            print("   ||2. Tim kiem can bo            ||")
            print("   ||3. Hien thi danh sach can bo  ||")
            print("   ||4. Thoat                      ||")
            print("   ||==============================||")
            lua_chon = input("Nhap lua chon (1-4): ").strip()
            if lua_chon == "1":
                self.them_moi()
            elif lua_chon == "2":
                self.tim_kiem()
            elif lua_chon == "3":
                self.hien_thi_ds()
            elif lua_chon == "4":
                print("Thoat chuong trinh. Tam biet!")
                break
            else:
                print("Lua chon khong hop le! Vui long thu lai.")
if __name__ == "__main__":
    QLCB().chay_menu()
