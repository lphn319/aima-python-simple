from search import UndirectedGraph

# Định nghĩa bản đồ Romania
romania_map = UndirectedGraph(dict(
    Arad=dict(Zerind=75, Sibiu=140, Timisoara=118),
    Bucharest=dict(Urziceni=85, Pitesti=101, Giurgiu=90, Fagaras=211),
    Craiova=dict(Drobeta=120, Rimnicu=146, Pitesti=138),
    Drobeta=dict(Mehadia=75),
    Eforie=dict(Hirsova=86),
    Fagaras=dict(Sibiu=99),
    Hirsova=dict(Urziceni=98),
    Iasi=dict(Vaslui=92, Neamt=87),
    Lugoj=dict(Timisoara=111, Mehadia=70),
    Oradea=dict(Zerind=71, Sibiu=151),
    Pitesti=dict(Rimnicu=97),
    Rimnicu=dict(Sibiu=80),
    Urziceni=dict(Vaslui=142)
))

# Vị trí của các thành phố trên bản đồ Romania
romania_map.locations = dict(
    Arad=(91, 492), Bucharest=(400, 327), Craiova=(253, 288),
    Drobeta=(165, 299), Eforie=(562, 293), Fagaras=(305, 449),
    Giurgiu=(375, 270), Hirsova=(534, 350), Iasi=(473, 506),
    Lugoj=(165, 379), Mehadia=(168, 339), Neamt=(406, 537),
    Oradea=(131, 571), Pitesti=(320, 368), Rimnicu=(233, 410),
    Sibiu=(207, 457), Timisoara=(94, 410), Urziceni=(456, 350),
    Vaslui=(509, 444), Zerind=(108, 531)
)

romania_city_name = dict(
    Arad=(-35, 0), Bucharest=(0, 15), Craiova=(-20, 15),
    Drobeta=(-50, 0), Eforie=(0, 15), Fagaras=(10, 0),
    Giurgiu=(10, 0), Hirsova=(10, 0), Iasi=(10, 0),
    Lugoj=(10, 0), Mehadia=(10, 0), Neamt=(10, -5),
    Oradea=(-50, 0), Pitesti=(-5, 20), Rimnicu=(10, -5),
    Sibiu=(0, -20), Timisoara=(-60, 0), Urziceni=(0, 15),
    Vaslui=(10, 0), Zerind=(-50, 0)
)

# Định nghĩa một bản đồ nhỏ khác
small_map = UndirectedGraph(dict(
    CityA=dict(CityB=50, CityC=80),
    CityB=dict(CityA=50, CityD=60),
    CityC=dict(CityA=80, CityD=70),
    CityD=dict(CityB=60, CityC=70)
))

# Vị trí của các thành phố trên bản đồ nhỏ
small_map.locations = dict(
    CityA=(100, 300), CityB=(200, 100),
    CityC=(400, 300), CityD=(300, 100)
)

small_city_name = dict(
    CityA=(0, -15), CityB=(0, -15),
    CityC=(0, 15), CityD=(0, -15)
)
# Định nghĩa bản đồ thành phố Hồ Chí Minh với kết nối mới từ Quận 5 đến Quận 4
hcm_map = UndirectedGraph(dict(
    District1=dict(District3=3, District4=2, BinhThanh=5),
    District3=dict(District1=3, District10=5, PhuNhuan=4),
    District4=dict(District1=2, District7=6, District5=3),  # Thêm kết nối từ Quận 4 đến Quận 5
    District5=dict(District10=5, District4=3),  # Thêm kết nối từ Quận 5 đến Quận 4
    District7=dict(NhaBe=8, District4=6),
    District10=dict(District3=5, District5=5, TanBinh=5, TanPhu=8),
    District12=dict(GoVap=6),
    BinhThanh=dict(District1=5, GoVap=5, PhuNhuan=5, ThuDuc=7),
    PhuNhuan=dict(District3=4, BinhThanh=5),
    TanBinh=dict(District10=5),
    TanPhu=dict(District10=8),
    GoVap=dict(District12=6, BinhThanh=5, ThuDuc=12),
    ThuDuc=dict(BinhThanh=7, GoVap=12),
    NhaBe=dict()
))

# Tọa độ giả định cho các quận trên bản đồ thành phố Hồ Chí Minh
hcm_map.locations = dict(
    District1=(800, 2500), 
    District3=(900, 2600), 
    District4=(950, 2400),  
    District5=(900, 2300),
    District7=(600, 2100),
    District10=(1150, 2200),
    District12=(2500, 3000),
    BinhThanh=(1500, 2700),
    PhuNhuan=(1600, 2600),
    TanBinh=(1300, 2800),
    TanPhu=(900, 1900),
    GoVap=(1700, 2900),
    ThuDuc=(2200, 2700),
    NhaBe=(500, 1700)
)

# Vị trí hiển thị tên cho các quận trong bản đồ thành phố Hồ Chí Minh
hcm_city_name = dict(
    District1=(0, -15), District3=(0, -15), District4=(0, -15),
    District5=(0, -15), District7=(0, -15), District10=(0, -15),
    District12=(0, 15),  # Tên Quận 12 hiển thị phía dưới điểm biểu diễn
    BinhThanh=(0, -15), PhuNhuan=(0, -15),
    TanBinh=(0, -15), TanPhu=(0, -15), GoVap=(0, -15),
    ThuDuc=(0, -15), NhaBe=(0, -15)
)

# Từ điển chứa các bản đồ để dễ truy cập
maps = {
    "Romania Map": (romania_map, romania_map.locations, romania_city_name),
    "Small Map": (small_map, small_map.locations, small_city_name),
    "Ho Chi Minh City Map": (hcm_map, hcm_map.locations, hcm_city_name)
}
