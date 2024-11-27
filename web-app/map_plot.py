import matplotlib.pyplot as plt
import numpy as np

def ve_ban_do(graph_dict, map_locations, city_name, xmin, xmax, ymin, ymax, start_city=None, dest_city=None):
    """
    Hàm ve_ban_do để vẽ bản đồ dựa trên thông tin các thành phố và kết nối giữa chúng.
    - graph_dict: Dictionary chứa thông tin về các kết nối giữa các thành phố (dạng đồ thị).
    - map_locations: Dictionary chứa tọa độ của các thành phố.
    - city_name: Dictionary chứa thông tin hiển thị tên thành phố (độ lệch dx, dy để vẽ tên).
    - xmin, xmax, ymin, ymax: Các giá trị tọa độ biên của bản đồ để xác định kích thước của biểu đồ.
    - start_city, dest_city: Tên của thành phố bắt đầu và kết thúc (nếu có).
    
    Quy trình vẽ:
    - Thiết lập kích thước của biểu đồ và đặt màu nền.
    - Vẽ từng thành phố với màu sắc khác nhau cho điểm bắt đầu (màu đỏ), điểm kết thúc (màu xanh lá), và các thành phố khác (màu vàng).
    - Hiển thị tên thành phố với font chữ nhỏ để dễ đọc.
    - Vẽ các đường kết nối giữa các thành phố.
    """
    fig, ax = plt.subplots()
    ax.axis([xmin-70, xmax+70, ymin-70, ymax+70])  # Đặt phạm vi của trục để có khoảng cách bao quanh bản đồ
    ax.set_facecolor('#f0f8ff')  # Đặt màu nền cho biểu đồ
    
    for key in graph_dict:
        x0, y0 = map_locations[key]
        
        # Vẽ điểm đại diện cho thành phố với các màu sắc khác nhau
        if key == start_city:
            ax.plot(x0, y0, 'o', color='#FF0000', markersize=8)  # Điểm bắt đầu màu đỏ
        elif key == dest_city:
            ax.plot(x0, y0, 'o', color='#00FF00', markersize=8)  # Điểm kết thúc màu xanh lá
        else:
            ax.plot(x0, y0, 'o', color='#FFD700', markersize=5)  # Các thành phố khác màu vàng

        # Vẽ tên thành phố với độ lệch dx, dy
        dx, dy = city_name[key]
        ax.text(x0 + dx, y0 - dy, key, fontsize=6, color='navy')

        # Vẽ các kết nối giữa các thành phố
        for neighbor in graph_dict[key]:
            x1, y1 = map_locations[neighbor]
            ax.plot([x0, x1], [y0, y1], color='#FFD700')  # Vẽ đường nối với màu vàng

    return fig

def ve_mui_ten(b, a, tx, ty, selected_map):
    """
    Hàm ve_mui_ten để vẽ mũi tên đại diện cho chuyển động giữa các thành phố.
    - b, a: Các hệ số cho biết hướng di chuyển từ điểm đầu đến điểm cuối (b = y2 - y1, a = x2 - x1).
    - tx, ty: Tọa độ của vị trí đích.
    - selected_map: Tên của bản đồ hiện tại để xác định hệ số phóng to cho mũi tên.
    
    Quy trình tính toán và vẽ mũi tên:
    - Tùy chỉnh hệ số phóng to mũi tên dựa trên bản đồ được chọn để đảm bảo kích thước phù hợp.
    - Tạo ma trận điểm cho các điểm của mũi tên (điểm gốc và ba điểm khác).
    - Sử dụng ma trận chuyển đổi để xoay và dịch chuyển các điểm của mũi tên đến vị trí đích.
    - Ma trận M1 dùng để tịnh tiến mũi tên đến vị trí (tx, ty).
    - Ma trận M2 dùng để xoay mũi tên theo góc theta được tính bằng arctan(b / a).
    - Áp dụng phép biến đổi affine để tính toán tọa độ mới của các điểm mũi tên.
    
    Trả về danh sách tọa độ các điểm của mũi tên đã được biến đổi.
    """
    # Tùy chỉnh hệ số phóng to mũi tên dựa trên bản đồ
    if selected_map == "Romania":
        scale_factor = 1.0  # Kích thước tiêu chuẩn cho bản đồ Romania
    elif selected_map == "Ho Chi Minh City":
        scale_factor = 2.5  # Kích thước nhỏ hơn cho bản đồ TP.HCM
    else:
        scale_factor = 0.75  # Kích thước mặc định cho các bản đồ khác

    # Ma trận các điểm của mũi tên
    p_mui_ten_ma_tran = [
        np.array([[0], [0], [1]], np.float32),
        np.array([[-20 * scale_factor], [10 * scale_factor], [1]], np.float32),
        np.array([[-15 * scale_factor], [0], [1]], np.float32),
        np.array([[-20 * scale_factor], [-10 * scale_factor], [1]], np.float32)
    ]
    
    # Ma trận tịnh tiến để di chuyển mũi tên đến vị trí (tx, ty)
    M1 = np.array([[1, 0, tx], [0, 1, ty], [0, 0, 1]], np.float32)
    # Tính góc xoay của mũi tên
    theta = np.arctan2(b, a)
    # Ma trận xoay mũi tên theo góc theta
    M2 = np.array([[np.cos(theta), -np.sin(theta), 0], [np.sin(theta), np.cos(theta), 0], [0, 0, 1]], np.float32)
    
    # Kết hợp hai phép biến đổi tịnh tiến và xoay
    M = np.matmul(M1, M2)
    # Tính toán tọa độ mới của các điểm của mũi tên sau khi biến đổi affine
    q_mui_ten = [np.matmul(M, p).flatten()[:2] for p in p_mui_ten_ma_tran]
    
    return q_mui_ten