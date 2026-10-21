# Tệp: src/cau09_thoi_gian.py
from datetime import datetime

# ------------------------------------------
# PHẦN 1: THỜI GIAN HIỆN TẠI VÀ ĐỊNH DẠNG CHUỖI
# ------------------------------------------
thoi_diem = datetime.now()
thoi_diem_text = thoi_diem.strftime("%Y-%m-%d %H:%M:%S")

print(thoi_diem)
print(type(thoi_diem))
print(thoi_diem_text)
print(type(thoi_diem_text))

print("-" * 40)

# ------------------------------------------
# PHẦN 2: TÍNH KHOẢNG THỜI GIAN (PHÉP TRỪ DATETIME)
# ------------------------------------------
# YÊU CẦU 24. DỰ ĐOÁN KẾT QUẢ PHÉP TRỪ:
# - bat_dau:  13:15 ngày 14/10/2026
# - ket_thuc: 15:05 ngày 14/10/2026
# - Tính toán: Từ 13:15 đến 15:05 là 1 giờ 50 phút (100 phút).
# - Dự đoán kết quả in ra: "1:50:00"
# - Dự đoán kiểu dữ liệu: <class 'datetime.timedelta'>

bat_dau = datetime(2026, 10, 14, 13, 15)
ket_thuc = datetime(2026, 10, 14, 15, 5)

thoi_luong = ket_thuc - bat_dau

print("Thời lượng:", thoi_luong)
print("Kiểu dữ liệu thời lượng:", type(thoi_luong))


# ==============================================================================
# YÊU CẦU 25. GIẢI THÍCH SỰ KHÁC NHAU GIỮA DATETIME, STR VÀ TIMEDELTA
# ==============================================================================
# 1. datetime (Ví dụ: thoi_diem, bat_dau, ket_thuc):
#    - Là kiểu dữ liệu biểu diễn một "MỐC THỜI GIAN" cụ thể (năm, tháng, ngày, giờ, phút, giây).
#    - Cho phép thực hiện các phép toán thời gian (như trừ hai mốc thời gian cho nhau).

# 2. str (Ví dụ: thoi_diem_text):
#    - Là kiểu "CHUỖI KÝ TỰ" đơn thuần thu được sau khi định dạng (strftime).
#    - Dùng để in ra màn hình hoặc lưu vào file/cơ sở dữ liệu cho người dùng dễ đọc.
#    - KHÔNG thể thực hiện trực tiếp các phép tính toán thời gian (cộng/trừ số giờ).

# 3. timedelta (Ví dụ: thoi_luong):
#    - Là kiểu dữ liệu biểu diễn một "KHOẢNG THỜI GIAN" (độ dài/khoảng cách giữa 2 mốc thời gian),
#      tính theo ngày, giây, microsecond.
#    - Kết quả của phép trừ giữa 2 đối tượng `datetime` sẽ tự động trả về kiểu `timedelta`.