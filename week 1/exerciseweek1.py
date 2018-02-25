#phan 1
# Số tiền An nhận được sau 15 năm gửi ngân hàng
print(1000 * 1.1**15)

#phan2

#2.1
# Khởi tạo biến savings có giá trị bằng 1000
savings = 1000
# In ra giá trị của biến savings
print(savings)

#2.2
# Khởi tạo biến savings
savings = 1000

# Khởi tạo biến factor biểu diễn lãi suất ngân hàng
factor = 1.1

# Tính toán số tiền và gán giá trị vào biến result
result = savings * factor**15 

# In ra giá trị của result
print(result)

#2.3
# Tạo biến desc
desc = "Data Science"

# Tạo biến profitable
profitable = True

print(desc)
print(profitable)

# In ra kiểu dữ liệu của biến savings
print(type(savings))

# In ra kiểu dữ liệu của biến factor
print(type(factor))

# In ra kiểu dữ liệu của biến desc
print(type(desc))

# In ra kiểu dữ liệu của biến profitable
print(type(profitable))

#2.4
# Các biến đã được khai báo sẵn cho bạn
savings = 1000
factor = 1.10
desc = "Data Science"

# Tính tích của savings và factor, lưu kết quả vào year1
year1 = savings * factor

# In ra kiểu dữ liệu của year1
print(type(year1))

# Tính tổng của desc và desc rồi lưu kết quả vào doubledesc
doubledesc = desc + desc 

# In ra doubledesc
print(doubledesc)

#2.5
# Khai báo biến savings và result
savings = 1000
result = 1000 * 1.10 ** 15

# Sửa lại lệnh in dưới đây cho đúng
print("Tôi gửi ngân hàng $" + str(savings) + ", sau 15 năm, bây giờ tôi đã có $" + str(result) + ". Tuyệt vời!")

# Khai báo pi_string
pi_string = "3.1415926"

# Chuyển pi_string sang float: pi_float
pi_float = float(pi_string)

#phan3

#3.1
# các biến thể hiện diện tích các phòng (m2)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# khởi tạo danh sách areas
areas = [hall,kit,liv,bed,bath]

# in ra areas
print(areas)

#3.2

# các biến thể hiện diện tích các phòng (m2)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# sửa lại dòng khởi tạo danh sách areas
areas = [hall, kit, "living room", liv, bed, "bathroom", bath]

# in ra areas
print(areas)

#3.3
# các biến thể hiện diện tích các phòng (m2)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# thông tin về ngôi nhà, biểu diễn bởi danh sách của các danh sách
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv]]

# in ra giá trị của house
print(house)

# in ra kiểu dữ liệu của house
print(type(house))

