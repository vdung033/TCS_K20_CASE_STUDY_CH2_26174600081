# ==========================================
# BÀI 3: TOÁN TỬ VÀ BIỂU THỨC (CÓ DỰ ĐOÁN)
# ==========================================

# Khai báo các biến đầu vào
tong_phut = 135
cong_suat_w = 250

# ------------------------------------------
# 9. Dùng // và % để tính giờ và phút
# ------------------------------------------
# DỰ ĐOÁN: 
# - 135 // 60 chia lấy nguyên  => 2 (giờ)
# - 135 % 60  chia lấy phần dư => 15 (phút)

gio = tong_phut // 60      # Kết quả thực tế: 2
phut_du = tong_phut % 60   # Kết quả thực tế: 15

print(f"9. Tổng thời gian: {gio} giờ {phut_du} phút")


# ------------------------------------------
# 10. Biểu thức so sánh: tong_phut > 60
# ------------------------------------------
# DỰ ĐOÁN: 135 > 60 là ĐÚNG => True

su_dung_lau = tong_phut > 60 # Kết quả thực tế: True

print(f"10. Sử dụng lâu (>60 phút): {su_dung_lau}")


# ------------------------------------------
# 11. Biểu thức logic: cong_suat_w > 0 và tong_phut > 0
# ------------------------------------------
# DỰ ĐOÁN: (250 > 0) là True AND (135 > 0) là True => True

du_lieu_hop_le = (cong_suat_w > 0) and (tong_phut > 0) # Kết quả thực tế: True

print(f"11. Dữ liệu hợp lệ: {du_lieu_hop_le}")


# ------------------------------------------
# 12. Dự đoán và kiểm chứng thứ tự ưu tiên toán tử
# ------------------------------------------
# DỰ ĐOÁN bt1: Phép nhân '*' tính trước -> 20 * 3 = 60, sau đó 100 + 60 => 160
# DỰ ĐOÁN bt2: Trong ngoặc '()' tính trước -> 100 + 20 = 120, sau đó 120 * 3 => 360

bt1 = 100 + 20 * 3    # Kết quả thực tế: 160
bt2 = (100 + 20) * 3  # Kết quả thực tế: 360

print(f"12a. Kết quả 100 + 20 * 3: {bt1} (Dự đoán: 160)")
print(f"12b. Kết quả (100 + 20) * 3: {bt2} (Dự đoán: 360)")