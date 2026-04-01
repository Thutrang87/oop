import math
class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    def hien_thi(self):
        print(f"Toạ độ điểm: ({self.x}, {self.y})")
    def doi_xung_qua_O(self):
        return Point(-self.x, -self.y)
    def khoang_cach_den_O(self):
        return math.sqrt(self.x**2 + self.y**2)
    def khoang_cach_den_diem(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
A = Point (3, 4)
print("Điểm A:", end= "")
A.hien_thi()

xb = int(input("Nhập tọa độ x của B: "))
yb = int (input("Nhập tọa độ y của B: "))
B = Point (xb, yb)

C = B.doi_xung_qua_O()
print(f"Điểm C (đối xứng B qua O): ({C.x}, {C.y})")
print(f"Khoảng cách B đến O: {B.khoang_cach_den_O():.2f}")
print(f"Khoảng cách A đến B: {A.khoang_cach_den_diem(B):.2f}")


