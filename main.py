from src.lotto_generator import generate_lotto_numbers, save_to_file

if __name__ == "__main__":
    lotto_numbers = generate_lotto_numbers()
    print("이번 주 로또 번호:", lotto_numbers)
    
    filename = save_to_file(lotto_numbers)
    print(f"번호가 {filename} 파일에 저장되었습니다.")
