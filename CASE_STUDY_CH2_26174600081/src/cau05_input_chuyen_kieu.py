# 17. Nhập dữ liệu từ bàn phím và kiểm tra kiểu dữ liệu ban đầu
ma_may = input("Nhập mã máy: ")
print("-> Kiểu dữ liệu mã máy:", type(ma_may))

cong_suat_input = input("Nhập công suất (W): ")
print("-> Kiểu dữ liệu công suất ban đầu:", type(cong_suat_input))

so_phut_input = input("Nhập số phút sử dụng: ")
print("-> Kiểu dữ liệu số phút ban đầu:", type(so_phut_input))

don_gia_input = input("Nhập đơn giá điện (VNĐ/kWh): ")
print("-> Kiểu dữ liệu đơn giá ban đầu:", type(don_gia_input))

print("-" * 40)

# 18. Chuyển kiểu dữ liệu (Type Casting)
cong_suat_w = float(cong_suat_input)   # Chuyển sang float
so_phut = int(so_phut_input)            # Chuyển sang int
don_gia_kwh = float(don_gia_input)      # Chuyển sang float

# 19. Tính lại điện năng tiêu thụ và chi phí điện
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

# In kết quả sau khi chuyển kiểu và tính toán
print("--- KẾT QUẢ TÍNH TOÁN ---")
print(f"Mã máy: {ma_may}")
print(f"Điện năng tiêu thụ: {dien_nang_kwh} kWh (Kiểu: {type(dien_nang_kwh)})")
print(f"Chi phí điện: {chi_phi:,.0f} VNĐ (Kiểu: {type(chi_phi)})")