from datetime import datetime

# ==========================================
# 1. NHẬP DỮ LIỆU TỪ BÀN PHÍM
# ==========================================
ma_phien = input("Nhập mã phiên: ")
ma_may = input("Nhập mã máy: ")
cong_suat_input = input("Nhập công suất (W): ")
thoi_gian_input = input("Nhập thời gian sử dụng (phút): ")
don_gia_input = input("Nhập đơn giá điện (VND/kWh): ")

# ==========================================
# 2. CHUYỂN ĐỔI KIỂU DỮ LIỆU (TYPE CASTING)
# ==========================================
cong_suat_w = float(cong_suat_input)
thoi_gian_phut = int(thoi_gian_input)
don_gia_kwh = float(don_gia_input)

# ==========================================
# 3. TÍNH TOÁN VÀ TẠO CÁC GIÁ TRỊ TỰ ĐỘNG
# ==========================================
# Tính điện năng tiêu thụ (kWh) và chi phí điện (VND)
dien_nang_kwh = cong_suat_w * thoi_gian_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

# Giá trị Boolean kiểm tra thời gian sử dụng trên 60 phút
tren_60_phut = thoi_gian_phut > 60

# Lấy thời điểm ghi nhận hiện tại và định dạng YYYY-MM-DD HH:MM:SS
thoi_diem_ghi_nhan = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# ==========================================
# 4. XUẤT KẾT QUẢ ĐỊNH DẠNG BẰNG F-STRING
# ==========================================
print("\n" + "=" * 40)
print(f"Mã phiên: {ma_phien}")
print(f"Máy: {ma_may}")
print(f"Công suất: {cong_suat_w:.2f} W")
print(f"Thời lượng: {thoi_gian_phut} phút")
print(f"Điện năng: {dien_nang_kwh:.3f} kWh")
print(f"Chi phí: {chi_phi:.2f} VND")
print(f"Trên 60 phút: {tren_60_phut}")
print(f"Ghi nhận lúc: {thoi_diem_ghi_nhan}")
print("=" * 40)