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

# Định nghĩa bản đồ nhỏ khác
small_map = UndirectedGraph(dict(
    CityA=dict(CityB=50, CityC=80),
    CityB=dict(CityA=50, CityD=60),
    CityC=dict(CityA=80, CityD=70),
    CityD=dict(CityB=60, CityC=70)
))

small_map.locations = dict(
    CityA=(100, 300), CityB=(200, 100),
    CityC=(400, 300), CityD=(300, 100)
)

small_city_name = dict(
    CityA=(0, -15), CityB=(0, -15),
    CityC=(0, 15), CityD=(0, -15)
)

# Định nghĩa bản đồ thành phố Hồ Chí Minh
hcm_map = UndirectedGraph(dict(
    District1=dict(District3=3, District4=2, BinhThanh=5),
    District3=dict(District1=3, District10=5, PhuNhuan=4),
    District4=dict(District1=2, District7=6, District5=3),
    District5=dict(District10=5, District4=3),
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

hcm_map.locations = dict(
    District1=(800, 2500), District3=(900, 2600), District4=(950, 2400),
    District5=(900, 2300), District7=(600, 2100), District10=(1150, 2200),
    District12=(2500, 3000), BinhThanh=(1500, 2700), PhuNhuan=(1600, 2600),
    TanBinh=(1300, 2800), TanPhu=(900, 1900), GoVap=(1700, 2900),
    ThuDuc=(2200, 2700), NhaBe=(500, 1700)
)

hcm_city_name = dict(
    District1=(-170, 0), District3=(0, -15), District4=(0, -15),
    District5=(20, -15), District7=(50, 0), District10=(20, -15),
    District12=(-110, 60), BinhThanh=(50, -15), PhuNhuan=(0, -15),
    TanBinh=(0, 50), TanPhu=(40, -15), GoVap=(0, -30),
    ThuDuc=(0, -15), NhaBe=(20, -20)
)

northern_vietnam_map = UndirectedGraph(dict(
    HaNoi=dict(BacNinh=30, VinhPhuc=50, HaNam=60, HungYen=40),
    BacNinh=dict(HaNoi=30, QuangNinh=100),
    VinhPhuc=dict(HaNoi=50, PhuTho=60, ThaiNguyen=70),
    PhuTho=dict(VinhPhuc=60, TuyenQuang=80, YenBai=100),
    ThaiNguyen=dict(VinhPhuc=70, TuyenQuang=60, BacKan=90),
    TuyenQuang=dict(ThaiNguyen=60, HaGiang=100, YenBai=80),
    HaGiang=dict(TuyenQuang=100, CaoBang=150),
    CaoBang=dict(HaGiang=150, BacKan=120),
    BacKan=dict(ThaiNguyen=90, CaoBang=120),
    YenBai=dict(PhuTho=100, LaoCai=120, SonLa=130),
    LaoCai=dict(YenBai=120, DienBien=180),
    SonLa=dict(YenBai=130, DienBien=150, HoaBinh=90),
    DienBien=dict(LaoCai=180, SonLa=150),
    HoaBinh=dict(SonLa=90, HaNoi=80),
    HaNam=dict(HaNoi=60, NinhBinh=70),
    NinhBinh=dict(HaNam=70),
    HungYen=dict(HaNoi=40, HaiDuong=50),
    HaiDuong=dict(HungYen=50, HaiPhong=70),
    HaiPhong=dict(HaiDuong=70, QuangNinh=80),
    QuangNinh=dict(BacNinh=100, HaiPhong=80)
))

# Tọa độ x, y cho các tỉnh miền Bắc Việt Nam
northern_vietnam_map.locations = dict(
    HaNoi=(400, 300), BacNinh=(450, 290), VinhPhuc=(350, 320),
    PhuTho=(300, 340), ThaiNguyen=(400, 350), TuyenQuang=(350, 380),
    HaGiang=(300, 420), CaoBang=(500, 420), BacKan=(450, 360),
    YenBai=(250, 360), LaoCai=(200, 400), SonLa=(150, 320),
    DienBien=(100, 300), HoaBinh=(250, 280), HaNam=(400, 250),
    NinhBinh=(350, 230), HungYen=(430, 270), HaiDuong=(470, 260),
    HaiPhong=(500, 240), QuangNinh=(550, 220)
)

northern_city_name = dict(
    HaNoi=(0, -15), BacNinh=(0, 0), VinhPhuc=(-25, 15),
    PhuTho=(-30, 10), ThaiNguyen=(0, 5), TuyenQuang=(0,0),
    HaGiang=(-15, -10), CaoBang=(5, -10), BacKan=(5, 0),
    YenBai=(-15, 15), LaoCai=(-15, -10), SonLa=(-10, 15),
    DienBien=(0, 15), HoaBinh=(-25, -15), HaNam=(-40, 0),
    NinhBinh=(0, 10), HungYen=(-50, 0), HaiDuong=(0, 0),
    HaiPhong=(-50, 5), QuangNinh=(0, 0)
)

# Định nghĩa bản đồ miền Tây
western_vietnam_map = UndirectedGraph(dict(
    LongAn=dict(TienGiang=30, DongThap=50),
    TienGiang=dict(LongAn=30, BenTre=40, VinhLong=50, DongThap=60),
    BenTre=dict(TienGiang=40, TraVinh=70),
    DongThap=dict(LongAn=50, TienGiang=60, AnGiang=80, CanTho=90),
    VinhLong=dict(TienGiang=50, TraVinh=60, CanTho=40),
    TraVinh=dict(BenTre=70, VinhLong=60, SocTrang=50),
    CanTho=dict(DongThap=90, VinhLong=40, HauGiang=30, SocTrang=60),
    HauGiang=dict(CanTho=30, SocTrang=40, BacLieu=80),
    SocTrang=dict(TraVinh=50, CanTho=60, HauGiang=40, BacLieu=70),
    AnGiang=dict(DongThap=80, KienGiang=100, CanTho=100),
    KienGiang=dict(AnGiang=100, BacLieu=90, CaMau=120),
    BacLieu=dict(HauGiang=80, SocTrang=70, KienGiang=90, CaMau=100),
    CaMau=dict(BacLieu=100, KienGiang=120)
))

# Tọa độ x, y cho các tỉnh miền Tây Việt Nam
western_vietnam_map.locations = dict(
    LongAn=(100, 500), TienGiang=(150, 450), BenTre=(200, 400),
    DongThap=(100, 550), VinhLong=(150, 400), TraVinh=(250, 350),
    CanTho=(200, 450), HauGiang=(250, 500), SocTrang=(300, 450),
    AnGiang=(50, 600), KienGiang=(50, 700), BacLieu=(300, 600),
    CaMau=(350, 700)
)

# Định nghĩa vị trí nhãn của các tỉnh
western_city_name = dict(
    LongAn=(0, -10), TienGiang=(10, -10), BenTre=(10, 0),
    DongThap=(-10, 10), VinhLong=(10, -10), TraVinh=(10, -10),
    CanTho=(0, 15), HauGiang=(10, 0), SocTrang=(10, 0),
    AnGiang=(-10, 15), KienGiang=(-10, 20), BacLieu=(10, 15),
    CaMau=(10, 20)
)

# Định nghĩa bản đồ Phú Yên
phu_yen_map = UndirectedGraph(dict(
    SongCau=dict(DongXuan=30, TuyAn=40),
    DongXuan=dict(SongCau=30, SonHoa=50, TuyAn=60),
    TuyAn=dict(SongCau=40, DongXuan=60, PhuHoa=30, TuyHoa=35),
    PhuHoa=dict(TuyAn=30, TuyHoa=20, SongHinh=50),
    TuyHoa=dict(PhuHoa=20, TuyAn=35, DongHoa=25),
    SongHinh=dict(PhuHoa=50, SonHoa=60, DongHoa=40),
    DongHoa=dict(TuyHoa=25, SongHinh=40),
    SonHoa=dict(DongXuan=50, SongHinh=60)
))

# Tọa độ x, y cho các huyện và thành phố trong tỉnh Phú Yên
phu_yen_map.locations = dict(
    SongCau=(500, 100), DongXuan=(450, 200), TuyAn=(600, 150),
    PhuHoa=(650, 250), TuyHoa=(700, 300), SongHinh=(400, 400),
    DongHoa=(800, 350), SonHoa=(350, 300)
)

# Định nghĩa vị trí nhãn của các huyện và thành phố
phu_yen_city_name = dict(
    SongCau=(0, -10), DongXuan=(0, 10), TuyAn=(0, -10),
    PhuHoa=(0, 10), TuyHoa=(0, -10), SongHinh=(0, 10),
    DongHoa=(0, -10), SonHoa=(0, 10)
)

# Tổng hợp các bản đồ
map_options = {
    "Romania": romania_map,
    "Small Map": small_map,
    "Ho Chi Minh City": hcm_map,
    "Northern Vietnam": northern_vietnam_map,
    "Western Vietnam": western_vietnam_map,
    "Phu Yen": phu_yen_map
}

map_locations_options = {
    "Romania": romania_map.locations,
    "Small Map": small_map.locations,
    "Ho Chi Minh City": hcm_map.locations,
    "Northern Vietnam": northern_vietnam_map.locations,
    "Western Vietnam": western_vietnam_map.locations,
    "Phu Yen": phu_yen_map.locations
}

city_name_options = {
    "Romania": romania_city_name,
    "Small Map": small_city_name,
    "Ho Chi Minh City": hcm_city_name,
    "Northern Vietnam": northern_city_name,
    "Western Vietnam": western_city_name,
    "Phu Yen": phu_yen_city_name
}
