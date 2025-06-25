# Add2Num
Hàm cài đặt thuật toán cộng 2 số lớn

## Hướng dẫn sử dụng

### 1. Yêu cầu môi trường
- Python 3.6 trở lên (đã kiểm tra với Python 3.13.4)
- Không cần cài thêm thư viện ngoài

### 2. Cấu trúc dự án
- `Add2Num.py`: Chứa lớp `MyBigNumber` và hàm cộng số lớn.
- `TestAdd2Num`: Chứa các test case kiểm thử tự động bằng unittest.

### 3. Cách chạy chương trình và kiểm thử

#### a. Chạy kiểm thử tự động (Test Case)
Mở terminal tại thư mục dự án và chạy lệnh sau:

```powershell
C:/Users/HP/AppData/Local/Programs/Python/Python313/python.exe TestAdd2Num
```

Nếu muốn xem chi tiết hơn:
```powershell
C:/Users/HP/AppData/Local/Programs/Python/Python313/python.exe -m unittest -v TestAdd2Num
```

#### b. Sử dụng trực tiếp hàm cộng số lớn
Bạn có thể import và sử dụng lớp `MyBigNumber` trong file Python khác:

```python
from Add2Num import MyBigNumber

big_num = MyBigNumber()
result = big_num.sum("123456789", "987654321")
print(result)  # Kết quả: 1111111110
```

### 4. Ghi chú
- Các test case nằm trong file `TestAdd2Num`.
- Nếu gặp lỗi về version Python, kiểm tra lại đường dẫn python hoặc cài đặt Python mới nhất.
- Nếu muốn thêm test case, chỉnh sửa file `TestAdd2Num` theo chuẩn unittest.
