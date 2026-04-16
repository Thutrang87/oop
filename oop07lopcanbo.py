from abc import ABC, abstractmethod
import json
import csv

class CanBo(ABC):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi):
        self.__ho_ten = ho_ten
        self.__tuoi = tuoi
        self.__gioi_tinh = gioi_tinh
        self.__dia_chi = dia_chi

    @property
    def ho_ten(self): return self.__ho_ten
    @property
    def tuoi(self): return self.__tuoi
    @property
    def gioi_tinh(self): return self.__gioi_tinh
    @property
    def dia_chi(self): return self.__dia_chi

    @abstractmethod
    def mo_ta(self): pass
    @abstractmethod
    def to_dict(self): pass

    def hien_thi(self):
        print(self.__str__())
    def __str__(self):
        return (f"Họ tên: {self.ho_ten} | Tuổi: {self.tuoi} | "
                f"Giới tính: {self.gioi_tinh} | Địa chỉ: {self.dia_chi} | "
                f"{self.mo_ta()}")
    def __eq__(self, other):
        return isinstance(other, CanBo) and self.ho_ten == other.ho_ten
    def __lt__(self, other):
        return self.ho_ten < other.ho_ten
    def __repr__(self):
        return self.__str__()
    
    @staticmethod
    def from_dict(d):
        """Khôi phục đúng loại đối tượng theo trường 'loai'."""
        loai = d.get("loai", "")
        if loai == "CongNhan":
            return CongNhan(d["ho_ten"], int(d["tuoi"]), d["gioi_tinh"], d["dia_chi"], int(d["bac"]))
        elif loai == "KySu":
            return KySu(d["ho_ten"], int(d["tuoi"]), d["gioi_tinh"], d["dia_chi"], d["nganh"])
        elif loai == "NhanVien":
            return NhanVien(d["ho_ten"], int(d["tuoi"]), d["gioi_tinh"], d["dia_chi"], d["cong_viec"])
        else:
            raise ValueError(f"Loại không hợp lệ: {loai}")
class CongNhan(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, bac):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.__bac = bac 
    
    @property
    def bac(self): return self.__bac
    def mo_ta(self):
        return f"[Công Nhân] Bậc: {self.__bac}"
    def to_dict(self):
        return {
            "loai": "CongNhan",
            "ho_ten": self.ho_ten,
            "tuoi": self.tuoi,
            "gioi_tinh": self.gioi_tinh,
            "dia_chi": self.dia_chi,
            "bac": self.__bac        
        }

class KySu(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, nganh):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.__nganh = nganh
    @property
    def nganh(self): return self.__nganh
    def mo_ta(self):
        return f"[Kỹ Sư] Ngành:{self.__nganh}"
    def to_dict(self):
        return {
            "loai": "KySu",
            "ho_ten": self.ho_ten,
            "tuoi": self.tuoi,
            "gioi_tinh": self.gioi_tinh,
            "dia_chi": self.dia_chi,
            "nganh": self.__nganh
        }
    
class NhanVien(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, cong_viec):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.__cong_viec = cong_viec
    @property
    def cong_viec(self): return self.__cong_viec
    def mo_ta(self):
        return f"[Nhân Viên] Công việc: {self.__cong_viec}"
    def to_dict(self):
        return {
            "loai": "NhanVien",
            "ho_ten": self.ho_ten,
            "tuoi": self.tuoi,
            "gioi_tinh": self.gioi_tinh,
            "dia_chi": self.dia_chi,
            "cong_viec": self.__cong_viec
        }
    
class QuanLyCanBo:
    FILE_CSV = "canbo.csv"
    FILE_JSON = "canbo.json"
    def __init__(self):
        self.__ds: dict[str, CanBo] = {}
        self.__doc_csv()
    def __doc_csv(self):
        try:
            data = [cb.to_dict() for cb in self.__ds.values()]
            with open(self.FILE_JSON, "w", encording="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"[Lỗi lưu JSON] {e}")
    def __luu_json(self):
        try:
            data = [cb.to_dict() for cb in self.__ds.values()]
            with open(self.FILE_JSON, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"[Loi luu JSON] {e}")        
    def tai_json(self):
        try:
            with open(self.FILE_JSON, encoding="utf-8") as f:
                data = json.load(f)
            self.__ds.clear()
            for d in data:
                cb = CanBo.from_dict(d)
                self.__ds[cb.ho_ten] = cb
            print(f"Đã tải {len(self.__ds)} cán bộ từ {self.FILE_JSON}")
        except FileNotFoundError:
            print(f"[Thông báo] Chưa có file {self.FILE_JSON}.")  
        except (json.JSONDecodeError, ValueError) as e:
            print(f"[Lỗi tải JSON] {e}")      
    def them (self, can_bo: CanBo):
        self.__ds[can_bo.ho_ten] = can_bo
        self.__luu_json()
    def xoa (self, ho_ten: str) -> bool:
        if ho_ten in self.__ds:
            del self.__ds[ho_ten]
            self.__luu_json()
            return True
        return False
    def tim_ho_ten(self, tu_khoa: str) ->list:
        tk = tu_khoa.lower()
        return [cb for cb in self.__ds.values() if tk in cb.ho_ten.lower()]
    def tim_loai(self, loai: str) ->list:
        loai_map = {"congnhan": CongNhan, "kysu": KySu, "nhanvien": NhanVien}
        cls = loai_map.get(loai.lower().replace(" ",""))
        if cls is None:
            return[]
        return [cb for cb in self.__ds.values() if isinstance(cb, cls)]
    def top3_bac_luong(self) -> list:
        """In ra 3 cán bộ có bậc/lương cao nhất (CongNhan -> bac, KySu/NhanVien -> tuoi lam dai dien)."""
        def key_fn(cb):
            if isinstance(cb, CongNhan):
                return cb.bac
            return 0
        ds = sorted(self.__ds.values(), key=key_fn, reverse=True)
        return ds[:3]
    def hien_thi_ds(self):
        if not self.__ds:
            print("\nDanh sách trống!")
            return
        print(f"\n===== DANH SÁCH CÁN BỘ ({len(self.__ds)} nguoi) =====")
        for i, cb in enumerate(sorted(self.__ds.values()), 1):
            print(f"{i}. {cb}")
    def __nhap_can_bo(self):
        print("\n 1. Công nhân  2. Kỹ sư  3. Nhân viên")
        loai = input("Chọn loại (1-3): ").strip()
        ho_ten = input("Họ tên: ").strip()
        try:
            tuoi = int(input("Tuổi: "))
        except ValueError:
            print(" [Lỗi] Tuổi phải là số nguyên!")
            return None
        gioi_tinh = input("Giới tính: ").strip()
        dia_chi = input("Địa chỉ: ").strip()
        try:
            if loai =="1":
                bac = int(input("Bậc(1-10): "))
                return CongNhan(ho_ten, tuoi, gioi_tinh, dia_chi, bac)
            elif loai == "2":
                nganh = input("Ngành: ")
                return KySu(ho_ten, tuoi, gioi_tinh, dia_chi, nganh)
            elif loai == "3":
                cong_viec = input("Công việc: ")
                return NhanVien(ho_ten, tuoi, gioi_tinh, dia_chi, cong_viec)
            else:
                print("Lựa chọn không hợp lệ!")
                return None
        except ValueError as e:
            print(f"[Lỗi nhập dữ liệu] {e}")
            return None
    def chay_menu(self):
        while True:
            try:
                print("\n" + "=" * 45)
                print("||           QUẢN LÝ CÁN BỘ                ||")
                print("=" * 45)
                print("|| 1. Thêm cán bộ mới                      ||")
                print("|| 2. Xoá cán bộ                           ||")
                print("|| 3. Tìm kiếm theo họ tên                 ||")
                print("|| 4. Tìm kiếm theo loại                   ||")
                print("|| 5. Hiển thị danh sách cán bộ            ||")
                print("|| 6. Top 3 cán bộ bậc cao nhất            ||")
                print("|| 7. Tải lại từ JSON                      ||")
                print("|| 8. Thoát                                ||")
                print("=" * 45)
                choice = input("Nhập lựa chọn (1-8): ").strip()

                if choice == "1":
                    cb = self.__nhap_can_bo()
                    if cb:
                        self.them(cb)
                        print(f"Đã thêm: {cb}")
                elif choice == "2":
                    ten = input("Nhập họ tên cần xoá: ").strip() 
                    if self.xoa(ten):
                        print("Không tìm thấy cán bộ!")
                elif choice == "3":
                    tu_khoa = input("Nhập từ khoá họ tên: ").strip()
                    kq = self.tim_ho_ten(tu_khoa)
                    if kq:
                        print(f"Tìm thấy {len(kq)} kết quả: ")
                        for cb in kq: cb.hien_thi()
                    else:
                        print("Không tìm thấy!")  
                elif choice == "4":
                    print("Loại: CongNhan / KySu / NhanVien")
                    loai = input("Nhập loại: ").strip()
                    kq = self.tim_loai(loai)
                    if kq:
                        print(f"Tìm thấy {len(kq)} cán bộ loại {loai}: ")
                        for cb in kq: cb.hien_thi()
                    else: 
                        print("Không tìm thấy hoặc loại không hợp lệ!")
                elif choice == "5":
                    self.hien_thi_ds()
                elif choice == "6":
                    top = self.top3_bac_luong()
                    print("\n---- Top 3 Công Nhân bậc cao nhất ----") 
                    for i, cb in enumerate(top, 1):
                        print(f"{i}. {cb}")
                elif choice == "7":
                    self.tai_json()
                elif choice == "8":
                    print("Thoát chương trình. Tạm biệt!")
                    break
                else:
                    print("Lựa chọn không hợp lệ! Vui lòng thử lại.")
            except Exception as e:
                print(f"[Loi khong mong doi] {e}")
if __name__ == "__main__":
    QuanLyCanBo().chay_menu()
   

