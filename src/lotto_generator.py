import random
import os
from datetime import datetime

def generate_lotto_numbers():
    """ 1~45 사이의 숫자 중 랜덤으로 6개를 뽑아 정렬하여 반환 """
    return sorted(random.sample(range(1, 46), 6))

def save_to_file(numbers):
    """ result 폴더를 생성하고 날짜별로 로또 번호를 저장 """
    os.makedirs("result", exist_ok=True)  # result 폴더 생성 (이미 있으면 무시)
    
    date_str = datetime.now().strftime("%Y-%m-%d")  # YYYY-MM-DD 형식의 날짜 문자열
    filename = f"result/{date_str}.txt"  # 날짜별 파일명 설정
    
    with open(filename, "a") as file:
        file.write(", ".join(map(str, numbers)) + "\n")

    return filename
