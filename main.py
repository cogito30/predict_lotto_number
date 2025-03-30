import random

def generate_lotto_numbers():
    return sorted(random.sample(range(1, 46), 6))

if __name__ == "__main__":
    lotto_numbers = generate_lotto_numbers()
    print("이번 주 로또 번호:", lotto_numbers)
