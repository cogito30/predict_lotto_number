import random

def generate_lotto_numbers():
    """ 1~45 사이의 숫자 중 랜덤으로 6개를 뽑아 정렬하여 반환 """
    return sorted(random.sample(range(1, 46), 6))

def save_to_file(filename, numbers):
    """ 생성된 번호를 텍스트 파일에 저장 """
    with open(filename, "a") as file:
        file.write(", ".join(map(str, numbers)) + "\n")
