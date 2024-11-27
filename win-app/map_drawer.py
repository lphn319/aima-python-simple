import tkinter as tk
import numpy as np

def scale_locations(locations, width=900, height=530, margin=20):
    """
    Hàm scale_locations để chuyển đổi các tọa độ ban đầu của các thành phố sang tọa độ phù hợp với kích thước của canvas.
    - Đầu vào là dictionary locations chứa tên thành phố và tọa độ của chúng.
    - Tham số width và height là kích thước của canvas.
    - Tham số margin xác định lề của bản đồ trên canvas.
    
    Công thức tính tỉ lệ và offset:
    - Tính tọa độ nhỏ nhất và lớn nhất của trục x và y từ các thành phố.
    - Tính tỉ lệ scale_x và scale_y dựa trên khoảng cách giữa các tọa độ lớn nhất và nhỏ nhất của mỗi trục.
    - Sử dụng giá trị nhỏ nhất của scale_x và scale_y để duy trì tỉ lệ ban đầu của bản đồ.
    - Tính offset để căn giữa bản đồ trên canvas.
    
    Trả về dictionary scaled_locations chứa các tọa độ đã được thay đổi theo tỉ lệ và căn giữa.
    """
    min_x = min(loc[0] for loc in locations.values())
    max_x = max(loc[0] for loc in locations.values())
    min_y = min(loc[1] for loc in locations.values())
    max_y = max(loc[1] for loc in locations.values())
    
    scale_x = (width - 2 * margin) / (max_x - min_x)
    scale_y = (height - 2 * margin) / (max_y - min_y)
    scale = min(scale_x, scale_y)  # Dùng tỉ lệ nhỏ nhất để giữ tỉ lệ ban đầu của bản đồ
    
    offset_x = (width - (max_x - min_x) * scale) / 2
    offset_y = (height - (max_y - min_y) * scale) / 2

    scaled_locations = {}
    for city, (x, y) in locations.items():
        scaled_x = offset_x + (x - min_x) * scale
        scaled_y = height - (offset_y + (y - min_y) * scale)  # Lật trục y để phù hợp với hệ tọa độ của canvas
        scaled_locations[city] = (scaled_x, scaled_y)
    
    return scaled_locations

def draw_map(canvas, current_map, locations, city_name, start, dest, scaled_locations):
    """
    Hàm draw_map để vẽ bản đồ lên canvas.
    - Đầu vào gồm canvas để vẽ, current_map chứa các kết nối giữa các thành phố, locations chứa tọa độ gốc của các thành phố, và scaled_locations chứa tọa độ đã được thay đổi tỉ lệ.
    - Các thành phố được vẽ bằng các hình tròn nhỏ với các màu sắc khác nhau để phân biệt điểm bắt đầu, điểm kết thúc và các thành phố khác.
    - Các đường nối giữa các thành phố được vẽ để biểu thị các kết nối trong current_map.
    
    Quy trình vẽ:
    - Vẽ nền bản đồ bằng một hình chữ nhật.
    - Duyệt qua tất cả các thành phố và vẽ chúng trên canvas.
    - Sử dụng các hình tròn để đánh dấu vị trí của từng thành phố và sử dụng các đường để vẽ kết nối giữa các thành phố.
    """
    # Vẽ nền bản đồ
    canvas.create_rectangle(0, 0, 900, 530, fill="#F0F8FF")
    for city in current_map.graph_dict:
        x0, y0 = scaled_locations[city]
        
        # Vẽ thành phố với các màu sắc khác nhau cho điểm bắt đầu và điểm kết thúc
        if city == start:
            canvas.create_oval(x0 - 6, y0 - 6, x0 + 6, y0 + 6, fill='#FF0000', outline='#FF0000')  # Điểm bắt đầu màu đỏ
        elif city == dest:
            canvas.create_oval(x0 - 6, y0 - 6, x0 + 6, y0 + 6, fill='#00FF00', outline='#00FF00')  # Điểm kết thúc màu xanh lá
        else:
            canvas.create_oval(x0 - 4, y0 - 4, x0 + 4, y0 + 4, fill='#FFD700', outline='#FFD700')  # Các thành phố khác màu vàng
        
        # Hiển thị tên thành phố
        dx, dy = city_name[city]
        canvas.create_text(x0 + dx, y0 + dy, text=city, anchor=tk.W, font=("Helvetica", 10), fill='#000080')

        # Vẽ các kết nối giữa các thành phố
        for neighbor in current_map.graph_dict[city]:
            x1, y1 = scaled_locations[neighbor]
            canvas.create_line(x0, y0, x1, y1, fill='#FFD700', width=2)  # Vẽ đường nối giữa các thành phố
