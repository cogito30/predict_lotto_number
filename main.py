from src.lotto_generator import generate_lotto_numbers, save_to_file

if __name__ == "__main__":
    try:
        count = int(input("몇 개의 로또 번호를 생성하시겠습니까? (기본값: 1) ") or 1)
        count = max(1, count)  # 최소 1개 이상 생성하도록 설정
    except ValueError:
        print("잘못된 입력입니다. 기본값(1)으로 생성합니다.")
        count = 1

    lotto_numbers_list = [generate_lotto_numbers() for _ in range(count)]
    
    for idx, numbers in enumerate(lotto_numbers_list, start=1):
        print(f"{idx}번째 로또 번호:", numbers)
    
    filename = save_to_file(lotto_numbers_list)
    print(f"번호가 {filename} 파일에 저장되었습니다.")
