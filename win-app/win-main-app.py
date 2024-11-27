from search import astar_search, breadth_first_graph_search, depth_first_graph_search, GraphProblem
import tkinter as tk
import tkinter.ttk as ttk
import time
import numpy as np
from maps import maps  
from map_drawer import scale_locations, draw_map
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

class App(tk.Tk): 
    def __init__(self):
        super().__init__()
        self.current_map_key = "Romania Map"
        self.current_map, self.locations, self.city_name = maps[self.current_map_key]
        self.start = 'Arad'
        self.dest = 'Arad'
        self.path_location = None
        self.is_selecting_start = True  # Biến để xác định nếu đang chọn điểm bắt đầu

        self.title('Search')
        self.cvs_map = tk.Canvas(self, width=900, height=530, relief=tk.SUNKEN, border=1)
        self.scaled_locations = scale_locations(self.locations)
        self.draw_map()
        self.cvs_map.bind("<Button-1>", self.on_canvas_click)  # Thêm sự kiện nhấn chuột

        lbl_frm_menu = tk.LabelFrame(self)
        lbl_map = ttk.Label(lbl_frm_menu, text='Map')
        self.cbo_map = ttk.Combobox(lbl_frm_menu, values=list(maps.keys()))
        self.cbo_map.set(self.current_map_key)
        self.cbo_map.bind("<<ComboboxSelected>>", self.change_map)
        
        lbl_algorithm = ttk.Label(lbl_frm_menu, text='Algorithm')
        self.cbo_algorithm = ttk.Combobox(lbl_frm_menu, values=['A*', 'BFS', 'DFS'])
        self.cbo_algorithm.set('A*')  # Đặt giá trị mặc định là A*
        lbl_algorithm.grid(row=8, column=0, padx=5, pady=0, sticky=tk.W)
        self.cbo_algorithm.grid(row=9, column=0, padx=5, pady=5)

        lbl_start = ttk.Label(lbl_frm_menu, text='Start')
        lbl_dest = ttk.Label(lbl_frm_menu, text='Dest')
        self.cbo_start = ttk.Combobox(lbl_frm_menu)
        self.cbo_dest = ttk.Combobox(lbl_frm_menu)
        self.update_city_list()
        self.cbo_start.bind("<<ComboboxSelected>>", self.cbo_start_click)
        self.cbo_dest.bind("<<ComboboxSelected>>", self.cbo_dest_click)

        btn_direction = ttk.Button(lbl_frm_menu, text='Direction', command=self.btn_direction_click)
        btn_run = ttk.Button(lbl_frm_menu, text='Run', command=self.btn_run_click)

        lbl_map.grid(row=0, column=0, padx=5, pady=0, sticky=tk.W)
        self.cbo_map.grid(row=1, column=0, padx=5, pady=5)
        lbl_algorithm.grid(row=2, column=0, padx=5, pady=5)
        self.cbo_algorithm.grid(row=3, column=0, padx=5, pady=5)
        lbl_start.grid(row=4, column=0, padx=5, pady=0, sticky=tk.W)
        self.cbo_start.grid(row=5, column=0, padx=5, pady=5)
        lbl_dest.grid(row=6, column=0, padx=5, pady=0, sticky=tk.W)
        self.cbo_dest.grid(row=7, column=0, padx=5, pady=5)
        btn_direction.grid(row=8, column=0, padx=5, pady=5)
        btn_run.grid(row=9, column=0, padx=5, pady=5)

        self.cvs_map.grid(row=0, column=0, padx=5, pady=5)
        lbl_frm_menu.grid(row=0, column=1, padx=5, pady=7, sticky=tk.N)

    def on_canvas_click(self, event):
        """
        Hàm xử lý khi người dùng nhấn vào bản đồ trên giao diện.
        - Lấy vị trí của nhấn chuột và xác định thành phố gần nhất.
        - Nếu đang chọn điểm bắt đầu, cập nhật `start`, nếu không thì cập nhật `dest`.
        """
        clicked_point = (event.x, event.y)
        closest_city = min(self.scaled_locations, key=lambda city: self.distance(self.scaled_locations[city], clicked_point))

        # Xác định đang chọn điểm bắt đầu hay điểm kết thúc
        if self.is_selecting_start:
            self.start = closest_city
            self.cbo_start.set(closest_city)
            self.is_selecting_start = False  # Chuyển sang chọn điểm kết thúc
        else:
            self.dest = closest_city
            self.cbo_dest.set(closest_city)
            self.is_selecting_start = True  # Chuyển sang chọn điểm bắt đầu

        # Vẽ lại bản đồ để đánh dấu điểm mới
        self.cvs_map.delete(tk.ALL)
        self.draw_map()

    def distance(self, loc1, loc2):
        """
        Tính toán khoảng cách Euclidean giữa hai điểm `loc1` và `loc2`.
        Công thức: sqrt((x1 - x2)^2 + (y1 - y2)^2)
        - Đây là công thức khoảng cách Euclidean chuẩn trong hình học để tính khoảng cách giữa hai điểm trong không gian hai chiều.
        """
        return np.sqrt((loc1[0] - loc2[0]) ** 2 + (loc1[1] - loc2[1]) ** 2)

    def change_map(self, *args):
        """
        Hàm thay đổi bản đồ khi người dùng chọn bản đồ khác từ danh sách combobox.
        - Cập nhật bản đồ hiện tại và danh sách thành phố.
        - Vẽ lại bản đồ mới.
        """
        self.current_map_key = self.cbo_map.get()
        self.current_map, self.locations, self.city_name = maps[self.current_map_key]
        self.scaled_locations = scale_locations(self.locations)
        self.start, self.dest = list(self.city_name.keys())[0], list(self.city_name.keys())[0]
        self.update_city_list()
        self.cvs_map.delete(tk.ALL)
        self.draw_map()

    def update_city_list(self):
        """
        Cập nhật danh sách thành phố trong combobox khi người dùng chọn bản đồ khác.
        """
        lst_city = list(self.city_name.keys())
        self.cbo_start['values'] = lst_city
        self.cbo_dest['values'] = lst_city
        self.cbo_start.set(lst_city[0])
        self.cbo_dest.set(lst_city[0])

    def cbo_start_click(self, *args):
        """
        Hàm xử lý khi người dùng chọn điểm bắt đầu từ combobox.
        """
        self.start = self.cbo_start.get()

    def cbo_dest_click(self, *args):
        """
        Hàm xử lý khi người dùng chọn điểm kết thúc từ combobox.
        """
        self.dest = self.cbo_dest.get()

    def draw_map(self):
        """
        Vẽ bản đồ và các thành phố lên giao diện.
        """
        draw_map(self.cvs_map, self.current_map, self.locations, self.city_name, self.start, self.dest, self.scaled_locations)

    def btn_direction_click(self):
        """
        Hàm xử lý khi người dùng nhấn nút "Direction" để tìm đường đi giữa hai điểm bắt đầu và kết thúc.
        - Sử dụng thuật toán tìm kiếm được chọn để tìm đường đi.
        - Vẽ lại bản đồ với đường đi được đánh dấu.
        """
        self.cvs_map.delete(tk.ALL)
        self.draw_map()
        problem = GraphProblem(self.start, self.dest, self.current_map)
        
        algorithm = self.cbo_algorithm.get()
        if algorithm == 'A*':
            result = astar_search(problem)
        elif algorithm =='BFS':
            result = breadth_first_graph_search(problem)
        elif algorithm == 'DFS':
            result = depth_first_graph_search(problem)

        if result:
            path = result.path()
            self.path_location = [(self.scaled_locations[city.state][0], self.scaled_locations[city.state][1]) for city in path]

            # Vẽ đường dẫn với nét dày hơn và màu đỏ
            for i in range(len(self.path_location) - 1):
                x0, y0 = self.path_location[i]
                x1, y1 = self.path_location[i + 1]
                self.cvs_map.create_line(x0, y0, x1, y1, fill='red', width=3)

            # Tô màu đỏ cho điểm bắt đầu và màu xanh lá cho điểm kết thúc
            start_x, start_y = self.scaled_locations[self.start]
            dest_x, dest_y = self.scaled_locations[self.dest]
            self.cvs_map.create_oval(start_x - 6, start_y - 6, start_x + 6, start_y + 6, fill='#FF0000', outline='#FF0000')
            self.cvs_map.create_oval(dest_x - 6, dest_y - 6, dest_x + 6, dest_y + 6, fill='#00FF00', outline='#00FF00')

    def btn_run_click(self):
        """
        Hàm xử lý khi người dùng nhấn nút "Run" để mô phỏng chuyển động giữa các điểm trên đường đi.
        - Sử dụng vòng lặp để vẽ từng bước di chuyển giữa các thành phố trên đường đi.
        - Công thức tính khoảng cách d1: d1 = sqrt((x1 - x0)^2 + (y1 - y0)^2) để tính khoảng cách giữa hai điểm.
        - Số bước chuyển động N1: N1 = int(N * d1 / d), điều này giúp điều chỉnh số bước di chuyển tỉ lệ với khoảng cách giữa các điểm.
        - Công thức tính vị trí trung gian x, y: x = x0 + (x1 - x0) * t, y = y0 + (y1 - y0) * t, với t thay đổi từ 0 đến 1 để di chuyển từ điểm đầu đến điểm cuối.
        """
        bg_color = self.cvs_map['background']
        N, d = 21, 100
        L = len(self.path_location)
        for i in range(L - 1):
            x0, y0 = self.path_location[i]
            x1, y1 = self.path_location[i + 1]
            d1 = np.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)
            N1 = int(N * d1 / d)
            dt = 1.0 / (N1 - 1)
            for j in range(N1):
                t = j * dt
                x, y = x0 + (x1 - x0) * t, y0 + (y1 - y0) * t
                self.cvs_map.delete(tk.ALL)
                self.draw_map()
                self.cvs_map.create_line(self.path_location, fill='red')
                self.draw_arrow(y1 - y0, x1 - x0, x, y, '#FF0000')
                time.sleep(0.05)
                self.cvs_map.update()
                self.draw_arrow(y1 - y0, x1 - x0, x, y, bg_color)
        self.draw_arrow(y1 - y0, x1 - x0, x, y, '#FF0000')

    def draw_arrow(self, b, a, tx, ty, color):
        """
        Vẽ mũi tên để mô phỏng hướng di chuyển trên bản đồ.
        - Sử dụng ma trận chuyển đổi để quay và tịnh tiến mũi tên.
        - Ma trận M1: Ma trận tịnh tiến dùng để di chuyển mũi tên đến vị trí (tx, ty).
        - Ma trận M2: Ma trận quay với góc theta = arctan(b / a) dùng để điều chỉnh hướng của mũi tên.
        - Mũi tên được tạo ra bằng cách áp dụng phép biến đổi M = M1 * M2 lên các điểm của mũi tên ban đầu.
        """
        arrow_points = [np.array([[0], [0], [1]], np.float32),
                        np.array([[-20], [10], [1]], np.float32),
                        np.array([[-15], [0], [1]], np.float32),
                        np.array([[-20], [-10], [1]], np.float32)]
        M1 = np.array([[1, 0, tx], [0, 1, ty], [0, 0, 1]], np.float32)
        theta = np.arctan2(b, a)
        M2 = np.array([[np.cos(theta), -np.sin(theta), 0], [np.sin(theta), np.cos(theta), 0], [0, 0, 1]], np.float32)
        M = np.matmul(M1, M2)
        transformed_points = [(np.matmul(M, p)[0, 0], np.matmul(M, p)[1, 0]) for p in arrow_points]
        self.cvs_map.create_polygon(transformed_points, fill=color, outline=color)

if __name__ == "__main__":
    app = App()
    app.mainloop()
