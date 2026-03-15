import math
import time 

# exercise 1.2
#c1
seconds = 42 * 60 + 42
print(seconds)  
#c2
miles = 10 / 1.61
print(miles)  
#c3
total_seconds = 42 * 60 + 42  
distance_miles = 10 / 1.61     
pace_seconds = total_seconds / distance_miles  
pace_minutes = int(pace_seconds // 60)   
pace_secs    = int(pace_seconds % 60)    
print(f"Pace: {pace_minutes} phút {pace_secs} giây / dặm")
speed_mph = distance_miles / (total_seconds / 3600)
print(f"Tốc độ: {speed_mph:.2f} dặm/giờ")

# exercise 2.2
#c1
r = 5
volume = (4/3) *math.pi * r**3
print(f"Thể tích: {volume:.2f}")
#c2
cover_price = 24.95
discount = cover_price *0.60
shipping = 3 + 0.75*(60-1)
total = 60 * discount + shipping
print(f"Tổng chi phí: ${total:.2f}")
#c3
start = 6*60+52
total_minutes = 1*(8*60+15) + 3*(7*60+12) + 1*(8*60+15)
arrival = start + total_minutes
hours = int(arrival // 60)
minutes = int(arrival % 60)
print (f"Về nhà lúc: {hours}:{minutes:02d} AM")

# exercise 3.3
def draw_grid(rows, cols):
    cell_width = 4   
    cell_height = 4  
    for r in range(rows + 1):
        for c in range(cols + 1):
            print('+', end='')
            if c < cols:
                print(' -' * cell_width, end=' ')
        print()  
        if r < rows:
            for _ in range(cell_height):
                for c in range(cols + 1):
                    print('|', end='')
                    if c < cols:
                        print(' ' * (cell_width * 2), end='')
                print()
draw_grid(2, 2)
def draw_grid(rows, cols, cell_w=4, cell_h=4):
    h_line = ('+' + ' -' * cell_w) * cols + '+'
    v_line = ('|' + ' ' * (cell_w * 2)) * cols + '|'
    for r in range(rows + 1):
        print(h_line)                        
        if r < rows:
            for _ in range(cell_h):
                print(v_line)                
draw_grid(4, 4)

# exercise 5.1
epoch_seconds = time.time()
days = int(epoch_seconds // (24*60*60))
remaining = int(epoch_seconds % (24*60*60))
hours = remaining // 3600
minutes = (remaining % 3600) // 60
seconds = remaining % 60
print (f"Số ngày kể từ epoch: {days} ngày")
print (f"Thời gian hiện tại: {hours:02d}:{minutes:02d}:{seconds:02d} (UTC)")
