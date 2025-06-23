import logging

class MyBigNumber:
    def __init__(self):
        # Cấu hình logging
        logging.basicConfig(level=logging.INFO, format='%(message)s')
        self.logger = logging.getLogger(__name__)
    
    def sum(self, stn1, stn2):
        """
        Cộng 2 số lớn được biểu diễn dưới dạng chuỗi
        Thực hiện giống như học sinh tiểu học: từ phải sang trái
        """
        # Làm cho 2 chuỗi có độ dài bằng nhau bằng cách thêm số 0 vào đầu
        max_len = max(len(stn1), len(stn2))
        stn1 = stn1.zfill(max_len)
        stn2 = stn2.zfill(max_len)
        
        result = ""  # Kết quả cuối cùng
        carry = 0    # Số nhớ
        step = 1     # Bước thực hiện
        
        self.logger.info(f"Bắt đầu cộng {stn1} + {stn2}")
        self.logger.info("=" * 50)
        
        # Duyệt từ phải sang trái (từ cuối chuỗi về đầu)
        for i in range(max_len - 1, -1, -1):
            # Lấy từng ký số
            digit1 = int(stn1[i])
            digit2 = int(stn2[i])
            
            # Cộng từng ký số
            temp_sum = digit1 + digit2 + carry
            
            # Tính toán kết quả và số nhớ
            current_digit = temp_sum % 10
            new_carry = temp_sum // 10
            
            # Ghi log quá trình tính toán
            if carry == 0:
                self.logger.info(f"Bước {step}: Lấy {digit1} cộng với {digit2} được {digit1 + digit2}.")
            else:
                self.logger.info(f"Bước {step}: Lấy {digit1} cộng với {digit2} được {digit1 + digit2}. Cộng tiếp với nhớ {carry} được {temp_sum}")
            
            # Thêm ký số vào kết quả (vì đang đi từ phải sang trái nên thêm vào đầu)
            result = str(current_digit) + result
            
            self.logger.info(f"Lưu {current_digit} vào kết quả được kết quả mới là \"{result}\"")
            
            if new_carry > 0:
                self.logger.info(f"Ghi nhớ {new_carry}.")
            else:
                self.logger.info("Không có nhớ.")
                
            carry = new_carry
            step += 1
            self.logger.info("")
        
        # Nếu còn số nhớ cuối cùng
        if carry > 0:
            result = str(carry) + result
            self.logger.info(f"Còn nhớ {carry}, thêm vào đầu kết quả: \"{result}\"")
        
        self.logger.info("=" * 50)
        self.logger.info(f"Kết quả cuối cùng: {result}")
        
        return result

# Ví dụ sử dụng
if __name__ == "__main__":
    big_num = MyBigNumber()
    
    # Test với ví dụ trong đề bài
    print("=== TEST VỚI VÍ DỤ TRONG ĐỀ BÀI ===")
    result1 = big_num.sum("1234", "897")
    print(f"\nKết quả: 1234 + 897 = {result1}")
    
    print("\n" + "="*60 + "\n")
    