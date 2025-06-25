import logging

class MyBigNumber:
    def __init__(self):
        logging.basicConfig(level=logging.INFO, format='%(message)s')
        self.logger = logging.getLogger(__name__)
    
    def sum(self, stn1, stn2):
        max_len = max(len(stn1), len(stn2))
        stn1 = stn1.zfill(max_len)
        stn2 = stn2.zfill(max_len)
        
        result = ""  
        carry = 0    
        step = 1     
        
        self.logger.info(f"Bắt đầu cộng {stn1} + {stn2}")
        self.logger.info("=" * 50)
        
        for i in range(max_len - 1, -1, -1):
    
            digit1 = int(stn1[i])
            digit2 = int(stn2[i])
            
            temp_sum = digit1 + digit2 + carry
            
            current_digit = temp_sum % 10
            new_carry = temp_sum // 10
            
            if carry == 0:
                self.logger.info(f"Bước {step}: Lấy {digit1} cộng với {digit2} được {digit1 + digit2}.")
            else:
                self.logger.info(f"Bước {step}: Lấy {digit1} cộng với {digit2} được {digit1 + digit2}. Cộng tiếp với nhớ {carry} được {temp_sum}")
            
            result = str(current_digit) + result
            
            self.logger.info(f"Lưu {current_digit} vào kết quả được kết quả mới là \"{result}\"")
            
            if new_carry > 0:
                self.logger.info(f"Ghi nhớ {new_carry}.")
            else:
                self.logger.info("Không có nhớ.")
                
            carry = new_carry
            step += 1
            self.logger.info("")
        
        if carry > 0:
            result = str(carry) + result
            self.logger.info(f"Còn nhớ {carry}, thêm vào đầu kết quả: \"{result}\"")
        
        self.logger.info("=" * 50)
        self.logger.info(f"Kết quả cuối cùng: {result}")
        
        return result

if __name__ == "__main__":
    big_num = MyBigNumber()
    
    print("=== TEST VỚI VÍ DỤ TRONG ĐỀ BÀI ===")
    result1 = big_num.sum("1234", "897")
    print(f"\nKết quả: 1234 + 897 = {result1}")
    
    print("\n" + "="*60 + "\n")
    