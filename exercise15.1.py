import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class Rectangle:
    def __init__(self, corner, width, height):
        self.corner = corner
        self.width = width
        self.height = height 
class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
c = Circle(Point(150, 100), 75)
print(f"Circle: tâm ({c.center.x}, {c.center.y}), bán kính {c.radius}")
def distance(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)
def point_in_circle(circle, point):
    return distance(circle.center, point) <= circle.radius
def rect_in_circle(circle, rect):
    x = rect.corner.x 
    y = rect.corner.y
    w = rect.width
    h = rect.height
    corners = [
        Point (x,     y),
        Point (x + w, y),
        Point (x,     y + h),
        Point (x + w, y + h),
    ]
    return all(point_in_circle(circle, corner) for corner in corners)
def rect_circle_overlap_basic(circle, rect):
    x = rect.corner.x 
    y = rect.corner.y
    w = rect.width
    h = rect.height
    corners = [
        Point (x,     y),
        Point (x + w, y),
        Point (x,     y + h),
        Point (x + w, y + h),
    ]
    return any(point_in_circle(circle, corner) for corner in corners)
def rect_circle_overlap(circle, rect):
    cx = circle.center.x
    cy = circle.center.y
    x = rect.corner.x
    y = rect.corner.y
    nearest_x = max(x, min(cx, x + rect.width))
    nearest_y = max(y, min(cy, y + rect.height))
    nearest_point = Point(nearest_x, nearest_y)
    return distance(circle.center, nearest_point) <= circle.radius

print("\n--- Kiểm tra point_in_circle ---") 
p1 = Point(150, 100)   
p2 = Point(300, 100)   
print(f"P(150,100) trong circle: {point_in_circle(c, p1)}")   
print(f"P(300,100) trong circle: {point_in_circle(c, p2)}")   

print("\n--- Kiểm tra rect_in_circle ---")
r1 = Rectangle(Point(100, 60), 100, 80)   
r2 = Rectangle(Point(50,  50), 200, 150)  
print(f"Rect nhỏ hoàn toàn trong circle: {rect_in_circle(c, r1)}")   
print(f"Rect lớn hoàn toàn trong circle: {rect_in_circle(c, r2)}")   

print("\n--- Kiểm tra rect_circle_overlap ---")
r3 = Rectangle(Point(200, 100), 100, 100) 
r4 = Rectangle(Point(400, 400), 50,  50)  
print(f"Rect giao với circle: {rect_circle_overlap(c, r3)}")   
print(f"Rect không giao:      {rect_circle_overlap(c, r4)}")
