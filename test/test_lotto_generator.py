import os
import sys
import pytest

# src 디렉터리를 모듈 경로에 추가
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from lotto_generator import generate_lotto_numbers, save_to_file, load_existing_numbers

@pytest.mark.parametrize("trials", [1, 5, 10])
def test_generate_lotto_numbers(trials):
    """ 로또 번호가 6개이며, 1~45 범위 내에서 중복 없이 생성되는지 테스트 """
    for _ in range(trials):
        numbers = generate_lotto_numbers()
        assert len(numbers) == 6  # 6개 숫자가 생성되는지 확인
        assert len(set(numbers)) == 6  # 중복이 없는지 확인
        assert all(1 <= num <= 45 for num in numbers)  # 숫자가 1~45 범위인지 확인

def test_save_to_file():
    """ 로또 번호가 파일에 저장되고, 중복 없이 기록되는지 테스트 """
    test_filename = "result/test_lotto.txt"
    os.makedirs("result", exist_ok=True)  # 테스트용 폴더 생성

    # 테스트용 데이터 생성
    numbers_list = [
        [1, 2, 3, 4, 5, 6],
        [10, 20, 30, 40, 41, 42],
        [1, 2, 3, 4, 5, 6]  # 중복된 번호 (저장되지 않아야 함)
    ]

    # 첫 번째 저장 (파일명 직접 지정)
    save_to_file(numbers_list, filename=test_filename)

    # 파일 읽기
    saved_numbers = load_existing_numbers(test_filename)
    
    # 중복 방지가 제대로 동작하는지 확인
    assert len(saved_numbers) == 2  # 중복 번호(1,2,3,4,5,6)가 저장되지 않아야 함

    # 테스트 후 파일 삭제
    os.remove(test_filename)

def test_load_existing_numbers():
    """ 파일에서 기존 번호를 정확히 불러오는지 테스트 """
    test_filename = "result/test_load.txt"

    # 테스트 데이터 쓰기
    test_data = ["3, 5, 7, 9, 11, 13\n", "15, 20, 25, 30, 35, 40\n"]
    with open(test_filename, "w") as file:
        file.writelines(test_data)

    # 파일 읽기 테스트
    loaded_numbers = load_existing_numbers(test_filename)
    expected_numbers = {"3, 5, 7, 9, 11, 13", "15, 20, 25, 30, 35, 40"}

    assert loaded_numbers == expected_numbers  # 불러온 값이 올바른지 확인

    # 테스트 후 파일 삭제
    os.remove(test_filename)
