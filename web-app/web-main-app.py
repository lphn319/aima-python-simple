# -*- coding: utf-8 -*-
import streamlit as st
import streamlit.components.v1 as components
from matplotlib.animation import FuncAnimation
import numpy as np
from maps import map_options, map_locations_options, city_name_options  # Import các bản đồ
from search import GraphProblem
from algorithms import run_algorithm
from map_plot import ve_ban_do, ve_mui_ten

# Giao diện để chọn bản đồ
selected_map = st.selectbox('Chọn bản đồ:', list(map_options.keys()))

# Kiểm tra và lưu trạng thái bản đồ đã chọn
if "previous_selected_map" not in st.session_state:
    st.session_state["previous_selected_map"] = selected_map

# Nếu bản đồ được chọn thay đổi, vẽ lại bản đồ
if st.session_state["previous_selected_map"] != selected_map:
    st.session_state["flag_ve_ban_do"] = False
    st.session_state["previous_selected_map"] = selected_map

# Lấy thông tin bản đồ được chọn
current_map = map_options[selected_map]
map_locations = map_locations_options[selected_map]
city_name = city_name_options[selected_map]
graph_dict = current_map.graph_dict

lst_city = list(city_name.keys())
x_coords = [coord[0] for coord in map_locations.values()]
y_coords = [coord[1] for coord in map_locations.values()]
xmin, xmax = min(x_coords), max(x_coords)
ymin, ymax = min(y_coords), max(y_coords)

# Khởi tạo trạng thái session
if "flag_anim" not in st.session_state:
    st.session_state["flag_anim"] = False

if not st.session_state["flag_anim"]:
    if "flag_ve_ban_do" not in st.session_state or not st.session_state["flag_ve_ban_do"]:
        st.session_state["flag_ve_ban_do"] = True
        fig = ve_ban_do(graph_dict, map_locations, city_name, xmin, xmax, ymin, ymax)
        st.session_state['fig'] = fig
        st.pyplot(fig)
    else:
        st.pyplot(st.session_state['fig'])

    # Hiển thị hai selectbox trên cùng một hàng
    col1, col2 = st.columns(2)
    with col1:
        start_city = st.selectbox('Thành phố bắt đầu:', lst_city)
    with col2:
        dest_city = st.selectbox('Thành phố đích:', lst_city)

    selected_algorithm = st.selectbox('Chọn thuật toán:', ['A*', 'Breadth-First Search', 'Depth-First Search'])

    st.session_state['start_city'] = start_city
    st.session_state['dest_city'] = dest_city

    if st.button('Direction'):
        problem = GraphProblem(start_city, dest_city, current_map)
        solution = run_algorithm(problem, selected_algorithm)
        if solution:
            lst_path = solution.path()
            path_locations = {data.state: map_locations[data.state] for data in lst_path}
            lst_path_location_x = [path_locations[city][0] for city in path_locations]
            lst_path_location_y = [path_locations[city][1] for city in path_locations]

            fig = ve_ban_do(graph_dict, map_locations, city_name, xmin, xmax, ymin, ymax, start_city, dest_city)
            ax = fig.gca()
            ax.plot(lst_path_location_x, lst_path_location_y, 'r-', linewidth=2)
            st.session_state['fig'] = fig
            st.rerun()

    if st.button('Run'):
        problem = GraphProblem(start_city, dest_city, current_map)
        solution = run_algorithm(problem, selected_algorithm)
        if solution:
            lst_path = solution.path()
            path_locations = {data.state: map_locations[data.state] for data in lst_path}
            lst_path_location_x = [path_locations[city][0] for city in path_locations]
            lst_path_location_y = [path_locations[city][1] for city in path_locations]

            fig = ve_ban_do(graph_dict, map_locations, city_name, xmin, xmax, ymin, ymax, start_city, dest_city)
            ax = fig.gca()
            ax.plot(lst_path_location_x, lst_path_location_y, 'r-', linewidth=2)

            lst_vi_tri = []
            for i in range(len(lst_path_location_x) - 1):
                x1, y1 = lst_path_location_x[i], lst_path_location_y[i]
                x2, y2 = lst_path_location_x[i + 1], lst_path_location_y[i + 1]
                b, a = y2 - y1, x2 - x1
                lst_vi_tri.extend([ve_mui_ten(b, a, x1 + t * (x2 - x1), y1 + t * (y2 - y1), selected_map) for t in np.linspace(0, 1, 10)])

            red_polygon, = ax.fill([], [], color='red')

            def init():
                ax.axis([xmin-70, xmax+70, ymin-70, ymax+70])
                return red_polygon,

            def animate(i):
                red_polygon.set_xy(lst_vi_tri[i])
                return red_polygon,

            anim = FuncAnimation(fig, animate, frames=len(lst_vi_tri), init_func=init, repeat=False)
            st.session_state["flag_anim"] = True
            st.session_state['anim'] = anim
            st.rerun()
else:
    if st.session_state["flag_anim"]:
        components.html(st.session_state["anim"].to_jshtml(), height=550)
        if st.button('Reset'):
            st.session_state["flag_anim"] = False
            st.session_state["flag_ve_ban_do"] = False
            st.rerun()
