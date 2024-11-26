import tkinter as tk
import numpy as np

def scale_locations(locations, width=900, height=530, margin=20):
    min_x = min(loc[0] for loc in locations.values())
    max_x = max(loc[0] for loc in locations.values())
    min_y = min(loc[1] for loc in locations.values())
    max_y = max(loc[1] for loc in locations.values())
    
    scale_x = (width - 2 * margin) / (max_x - min_x)
    scale_y = (height - 2 * margin) / (max_y - min_y)
    scale = min(scale_x, scale_y)
    
    offset_x = (width - (max_x - min_x) * scale) / 2
    offset_y = (height - (max_y - min_y) * scale) / 2

    scaled_locations = {}
    for city, (x, y) in locations.items():
        scaled_x = offset_x + (x - min_x) * scale
        scaled_y = height - (offset_y + (y - min_y) * scale)
        scaled_locations[city] = (scaled_x, scaled_y)
    
    return scaled_locations

def draw_map(canvas, current_map, locations, city_name, start, dest, scaled_locations):
    canvas.create_rectangle(0, 0, 900, 530, fill="#F0F8FF")
    for city in current_map.graph_dict:
        x0, y0 = scaled_locations[city]
        
        # Draw cities with different colors for start and destination
        if city == start:
            canvas.create_oval(x0 - 6, y0 - 6, x0 + 6, y0 + 6, fill='#FF0000', outline='#FF0000')
        elif city == dest:
            canvas.create_oval(x0 - 6, y0 - 6, x0 + 6, y0 + 6, fill='#00FF00', outline='#00FF00')
        else:
            canvas.create_oval(x0 - 4, y0 - 4, x0 + 4, y0 + 4, fill='#FFD700', outline='#FFD700')
        
        dx, dy = city_name[city]
        canvas.create_text(x0 + dx, y0 + dy, text=city, anchor=tk.W, font=("Helvetica", 10), fill='#000080')

        for neighbor in current_map.graph_dict[city]:
            x1, y1 = scaled_locations[neighbor]
            canvas.create_line(x0, y0, x1, y1, fill='#FFD700', width=2)
