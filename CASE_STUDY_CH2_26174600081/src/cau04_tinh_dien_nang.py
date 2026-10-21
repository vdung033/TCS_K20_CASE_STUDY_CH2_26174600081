# ==========================================
# BÀI 4: TÍNH ĐIỆN NĂNG VÀ CHI PHÍ
# ==========================================

# ------------------------------------------
# 15. DỰ ĐOÁN KẾT QUẢ TRƯỚC KHIN CHẠY
# ------------------------------------------
# Với so_phut = 90:
# - dien_nang_kwh = 250 * 90 / 60 / 1000 = 22500 / 60 / 1000 = 0.375 (kWh)
# - chi_phi = 0.375 * 3000 = 1125.0 (VNĐ)
# - Kiểu dữ liệu: Cả hai đều có kiểu <class 'float'> (do có phép chia '/')
#
# Với so_phut = 60:
# - dien_nang_kwh = 250 * 60 / 60 / 1000 = 0.25 (kWh)
# - chi_phi = 0.25 * 3000 = 750.0 (VNĐ)


# ------------------------------------------
# 13 & 14. TRƯỜNG HỢP SO_PHUT = 90
# ------------------------------------------
cong_suat_w = 250
so_phut = 90
don_gia_kwh = 3000

# 13. Tính toán
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

# 14. In giá trị và kiểu dữ liệu
print("=== TRƯỜNG HỢP 1: so_phut = 90 ===")
print("Điện năng tiêu thụ:", dien_nang_kwh, "kWh | Kiểu:", type(dien_nang_kwh))
print("Chi phí điện:", chi_phi, "VNĐ | Kiểu:", type(chi_phi))


print("\n" + "-" * 40 + "\n")


# ------------------------------------------
# 16. THAY SO_PHUT BẰNG 60 VÀ CHẠY LẠI
# ------------------------------------------
so_phut = 60

# Tính toán lại
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

print("=== TRƯỜNG HỢP 2: so_phut = 60 ===")
print("Điện năng tiêu thụ:", dien_nang_kwh, "kWh | Kiểu:", type(dien_nang_kwh))
print("Chi phí điện:", chi_phi, "VNĐ | Kiểu:", type(chi_phi))