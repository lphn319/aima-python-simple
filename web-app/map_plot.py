import matplotlib.pyplot as plt
import numpy as np

def ve_ban_do(graph_dict, map_locations, city_name, xmin, xmax, ymin, ymax, start_city=None, dest_city=None):
    fig, ax = plt.subplots()
    ax.axis([xmin-70, xmax+70, ymin-70, ymax+70])
    ax.set_facecolor('#f0f8ff')
    for key in graph_dict:
        x0, y0 = map_locations[key]
        if key == start_city:
            ax.plot(x0, y0, 'o', color='#FF0000', markersize=8)
        elif key == dest_city:
            ax.plot(x0, y0, 'o', color='#00FF00', markersize=8)
        else:
            ax.plot(x0, y0, 'o', color='#FFD700', markersize=5)

        dx, dy = city_name[key]
        ax.text(x0 + dx, y0 - dy, key, fontsize=6, color='navy')

        for neighbor in graph_dict[key]:
            x1, y1 = map_locations[neighbor]
            ax.plot([x0, x1], [y0, y1], color='#FFD700')

    return fig

def ve_mui_ten(b, a, tx, ty, selected_map):
    # Tùy chỉnh hệ số phóng to mũi tên dựa trên bản đồ
    if selected_map == "Romania":
        scale_factor = 1.0  # Kích thước tiêu chuẩn cho bản đồ Romania
    elif selected_map == "Ho Chi Minh City":
        scale_factor = 2.5  # Kích thước nhỏ hơn cho bản đồ TP.HCM
    else:
        scale_factor = 0.75  # Kích thước mặc định cho các bản đồ khác

    p_mui_ten_ma_tran = [
        np.array([[0], [0], [1]], np.float32),
        np.array([[-20 * scale_factor], [10 * scale_factor], [1]], np.float32),
        np.array([[-15 * scale_factor], [0], [1]], np.float32),
        np.array([[-20 * scale_factor], [-10 * scale_factor], [1]], np.float32)
    ]
    M1 = np.array([[1, 0, tx], [0, 1, ty], [0, 0, 1]], np.float32)
    theta = np.arctan2(b, a)
    M2 = np.array([[np.cos(theta), -np.sin(theta), 0], [np.sin(theta), np.cos(theta), 0], [0, 0, 1]], np.float32)
    M = np.matmul(M1, M2)
    q_mui_ten = [np.matmul(M, p).flatten()[:2] for p in p_mui_ten_ma_tran]
    return q_mui_ten

