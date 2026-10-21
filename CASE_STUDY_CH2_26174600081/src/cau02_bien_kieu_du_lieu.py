# 5 & 6. Khai báo biến chuẩn snake_case và chọn kiểu dữ liệu phù hợp
session_id = "LAB026"       # Kiểu str (chuỗi ký tự)
machine_id = "PC12"         # Kiểu str (chuỗi ký tự)
power = 250.0               # Kiểu float (số thực)
duration = 90               # Kiểu int (số nguyên)
is_active = True            # Kiểu bool (bolean: True/False)
note = None                 # Kiểu NoneType (giá trị rỗng)

# 7. In từng giá trị và kiểm tra kiểu dữ liệu
print("Mã phiên:", session_id, "| Kiểu:", type(session_id))
print("Mã máy:", machine_id, "| Kiểu:", type(machine_id))
print("Công suất:", power, "W | Kiểu:", type(power))
print("Thời gian:", duration, "phút | Kiểu:", type(duration))
print("Trạng thái:", is_active, "| Kiểu:", type(is_active))
print("Ghi chú:", note, "| Kiểu:", type(note))

print("-" * 40) # Dòng phân cách

# 8. Gán lại giá trị thời gian và in ra giá trị mới
duration = 120
print("Thời gian sử dụng mới:", duration, "phút")