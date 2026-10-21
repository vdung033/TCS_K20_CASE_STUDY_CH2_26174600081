# Tệp: src/cau07_chan_doan_loi.py

# ==========================================
# ĐOẠN MÃ SAU KHỊ ĐÃ CHẨN ĐOÁN VÀ SỬA LỖI
# ==========================================
ma_may = input("Nhập mã máy: ")
cong_suat_w = float(input("Nhập công suất W: "))  # Đã sửa lỗi 2 (TypeError): ép kiểu sang float
so_phut = int(input("Nhập số phút: "))
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
print(f"Máy: {ma_may}")
print(f"Điện năng: {dien_nang_kwh:.3f} kWh")      # Đã sửa lỗi 1 (SyntaxError - thêm ngoặc) và lỗi 3 (NameError - đúng tên biến)


# ==============================================================================
# NHẬT KÝ CHẨN ĐOÁN VÀ QUÁ TRÌNH SỬA LỖI (YÊU CẦU 20 - 22)
# ==============================================================================
# LẦN CHẠY 1:
# - Tên tệp: src/cau07_chan_doan_loi.py
# - Số dòng: Dòng 6
# - Loại lỗi: SyntaxError
# - Thông báo lỗi: SyntaxError: '(' was never closed
# - Nguyên nhân: Câu lệnh print() ở dòng cuối bị thiếu dấu đóng ngoặc ')' ở cuối lệnh.
# - Cách sửa: Thêm dấu ngoặc đóng ')' vào cuối dòng 6 thành: print(f"Điện năng: {dien_nang:.3f} kWh")

# LẦN CHẠY 2 (Sau khi sửa SyntaxError):
# - Tên tệp: src/cau07_chan_doan_loi.py
# - Số dòng: Dòng 4
# - Loại lỗi: TypeError
# - Thông báo lỗi: TypeError: unsupported operand type(s) for /: 'str' and 'int'
# - Nguyên nhân: Biến cong_suat_w nhận dữ liệu từ hàm input() nên có kiểu chuỗi (str). Khi thực hiện phép chia '/' với số nguyên 60, Python sẽ báo lỗi vì không hỗ trợ chia chuỗi cho số.
# - Cách sửa: Ép kiểu dữ liệu sang số thực (float) ở dòng 2: cong_suat_w = float(input("Nhập công suất W: "))

# LẦN CHẠY 3 (Sau khi sửa TypeError):
# - Tên tệp: src/cau07_chan_doan_loi.py
# - Số dòng: Dòng 6
# - Loại lỗi: NameError
# - Thông báo lỗi: NameError: name 'dien_nang' is not defined
# - Nguyên nhân: Trong chuỗi f-string gọi tên biến 'dien_nang', nhưng tên biến thực tế đã tính toán ở dòng 4 là 'dien_nang_kwh'.
# - Cách sửa: Đổi tên biến trong ngoặc nhọn ở dòng 6 thành: print(f"Điện năng: {dien_nang_kwh:.3f} kWh")


# ==============================================================================
# TỔNG KẾT VÀ BÀI HỌC VỀ LỖI (YÊU CẦU 23)
# ==============================================================================
# Comment 1: Hàm input() luôn trả về kiểu dữ liệu chuỗi (str). Mọi biến dùng cho tính toán số học bắt buộc phải chuyển kiểu (float/int) trước khi thực hiện các phép toán (*, /).
# Comment 2: Luôn chú ý cú pháp đóng ngoặc ')' và đặt tên biến đồng nhất giữa bước tính toán và bước in đầu ra để tránh các lỗi cơ bản như SyntaxError và NameError.