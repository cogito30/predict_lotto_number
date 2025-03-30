import random
import os
from datetime import datetime

def generate_lotto_numbers():
    """ 1~45 사이의 숫자 중 랜덤으로 6개를 뽑아 정렬하여 반환 """
    return sorted(random.sample(range(1, 46), 6))

def load_existing_numbers(filename):
    """ 기존에 저장된 번호를 불러와 리스트로 반환 """
    if not os.path.exists(filename):
        return set()
    
    with open(filename, "r") as file:
        return {line.strip() for line in file.readlines()}  # 줄 단위로 읽어서 중복 확인

def save_to_file(numbers_list, filename=None):
    """ result 폴더를 생성하고 날짜별로 중복 없이 로또 번호 저장 """
    os.makedirs("result", exist_ok=True)  # result 폴더 생성 (이미 있으면 무시)

    # 기본값: 날짜별 저장 (테스트 시에는 파일명을 직접 지정할 수 있도록 변경)
    if filename is None:
        date_str = datetime.now().strftime("%Y-%m-%d")  # YYYY-MM-DD 형식의 날짜 문자열
        filename = f"result/{date_str}.txt"

    existing_numbers = load_existing_numbers(filename)  # 기존에 저장된 번호 불러오기
    new_numbers = {", ".join(map(str, numbers)) for numbers in numbers_list}

    unique_numbers = new_numbers - existing_numbers  # 기존 데이터와 중복되지 않는 번호만 선택

    if unique_numbers:
        with open(filename, "a") as file:
            for numbers in unique_numbers:
                file.write(numbers + "\n")
        print(f"{len(unique_numbers)}개의 새로운 로또 번호가 {filename} 파일에 저장되었습니다.")
    else:
        print("모든 번호가 이미 존재합니다. 새로운 번호가 저장되지 않았습니다.")

    return filename
