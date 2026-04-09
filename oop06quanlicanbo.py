from abc import ABC, abstractmethod
class CanBo(ABC):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi):
        self.__ho_ten = ho_ten
        self.__tuoi = tuoi
        self.__gioi_tinh = gioi_tinh
        self.__dia_chi = dia_chi
    @property
    def ho_ten(self):
        return self.__ho_ten
    @property
    def tuoi(self):
        return self.__tuoi
    @property
    def gioi_tinh(self):
        return self.__gioi_tinh
    @property
    def dia_chi(self):
        return self.__dia_chi
    @abstractmethod
    def mo_ta(self):
        pass
    def hien_thi(self):
        print(self.__str__())
    def __str__(self):
        return (f"Họ tên:{self.ho_ten} | Tuổi: {self.tuoi} | Giới tính: {self.gioi_tinh} | Địa chỉ: {self.dia_chi} | {self.mo_ta()}")
    def __eq__(self, other):
        return isinstance(other, CanBo) and self.ma_cb == other.ma_cb
    def __lt__(self, other):
        return self.__ho_ten < other.ho_ten
    def __repr__(self):
        return self.__str__()
class CongNhan(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, bac):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.__bac = bac
    def mo_ta(self):
        return f"[Công nhân] Bậc: {self.__bac}"
class KySu(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, nganh):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.__nganh= nganh
    def mo_ta(self):
        return f"[Kỹ sư] Ngành đào tạo: {self.__nganh}"
class NhanVien(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, cong_viec):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.__cong_viec = cong_viec
    def mo_ta(self):
        return f"[Nhân viên] Công việc: {self.__cong_viec}"
class QLCB:
    def __init__(self):
        self.__ds_can_bo = []
        self.__ds_can_bo.append(CongNhan("Nguyen Van A", 30, "Nam", "Hà Nội", 3))
        self.__ds_can_bo.append(KySu("Tran Thi B", 28, "Nữ", "HCM", "CNTT"))
        self.__ds_can_bo.append(NhanVien("Le Van C", 35, "Nam", "Đà Nẵng", "Hành chính"))
    def them_can_bo(self):
        print("\n===== Thêm cán bộ mới =====")
        print("Chọn loại cán bộ:")
        print("1. Công nhân")
        print("2. Kỹ sư")
        print("3. Nhân viên")
        choice = input("Nhập lựa chọn của bạn (1-3): ").strip()
        ho_ten = input("Họ tên: ")
        tuoi = int(input("Tuổi: "))
        gioi_tinh = input("Giới tính: ")
        dia_chi = input("Địa chỉ: ")
        if choice == "1":
            bac = int(input("Bậc(1-10): "))
            can_bo = CongNhan(ho_ten, tuoi, gioi_tinh, dia_chi, bac)
        elif choice == "2":
            nganh = input("Ngành: ")
            can_bo = KySu(ho_ten, tuoi, gioi_tinh, dia_chi, nganh)
        elif choice == "3":
            cong_viec = input("Công việc: ")
            can_bo = NhanVien(ho_ten, tuoi, gioi_tinh, dia_chi, cong_viec)
        else:
            print("Lựa chọn không hợp lệ!")
            return
        self.__ds_can_bo.append(can_bo)
        print(f"Đã thêm cán bộ: {can_bo}")
    def tim_kiem(self):
        print("\n===== Tìm kiếm cán bộ =====")
        keyword = input("Nhập tên cán bộ cần tìm: ").strip().lower()
        results = [cb for cb in self.__ds_can_bo if keyword in cb.ho_ten.lower()]
        if not results:
            print("Không tìm thấy cán bộ nào!")
        else:
            print(f"Tìm thấy {len(results)} kết quả:")
            for cb in results:
                print()
                cb.hien_thi()
    def hien_thi_ds(self):
        if not self.__ds_can_bo:
            print("Danh sách cán bộ trống!")
            return
        print(f"\n====== DANH SÁCH CÁN BỘ ({len(self.__ds_can_bo)} NGƯỜI) ======")
        for i, cb in enumerate(self.__ds_can_bo, 1):
            print(f"{i}. {cb}")
    def luu_file(self):
        with open("can_bo.csv", "w", encoding="utf-8") as f:
            for cb in self.__ds_can_bo:
                f.write(repr(cb) + "\n")
        print("Đã lưu danh sách cán bộ vào file canbo.txt")
    def chay_menu(self):
        while True:
            print("\n" + "=" * 40)
            print("||           QUẢN LÝ CÁN BỘ           ||")
            print("=" * 40)
            print("|| 1. Thêm cán bộ mới                 ||")
            print("|| 2. Tìm kiếm cán bộ                 ||")
            print("|| 3. Hiển thị danh sách cán bộ       ||")
            print("|| 4. Thoát                           ||")
            print("=" * 40)
            choice = input("Nhập lựa chọn của bạn (1-5): ").strip()
            if choice == "1":
                self.them_can_bo()
            elif choice == "2":
                self.tim_kiem()
            elif choice == "3":
                self.hien_thi_ds()
            elif choice == "4":
                print("Thoát chương trình. Hẹn gặp lại!")
                break
            else:
                print("Lựa chọn không hợp lệ! Vui lòng nhập lại.")
if __name__ == "__main__":
    QLCB().chay_menu()
