# Nhập dữ liệu đầu vào từ bàn phím
ma_phien = input("Nhập mã phiên: ")
ma_may = input("Nhập mã máy: ")
cong_suat_w = float(input("Nhập công suất (W): "))
so_phut = float(input("Nhập số phút sử dụng: "))
don_gia_kwh = float(input("Nhập đơn giá (VNĐ/kWh): "))

# Tính toán điện năng (kWh) và chi phí (VNĐ)
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

# In kết quả ra màn hình theo đúng định dạng tối thiểu
print(f"Mã phiên: {ma_phien}")
print(f"Máy: {ma_may}")
print(f"Điện năng: {dien_nang_kwh}")
print(f"Chi phí: {chi_phi}")