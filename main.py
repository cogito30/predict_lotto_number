import random

def generate_lotto_numbers():
    return sorted(random.sample(range(1, 46), 6))

def save_to_file(filename, numbers):
    with open(filename, "a") as file:
        file.write(", ".join(map(str, numbers)) + "\n")

if __name__ == "__main__":
    lotto_numbers = generate_lotto_numbers()
    print("이번 주 로또 번호:", lotto_numbers)
    
    save_to_file("lotto_history.txt", lotto_numbers)
    print("번호가 lotto_history.txt 파일에 저장되었습니다.")
