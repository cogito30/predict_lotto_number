# Lotto Predictor
- 로또 번호 생성기

## Function
- 랜덤 번호 생성 개수(기본값 1) 지정 및 생성
- 생성된 번호 저장
- 


## How To Use
- create virtual environment
```
conda create -n py13 python=3.13
```
- activate virtual environment
```
conda activate py13
```
- install framework/library
```
pip install pytest
```
- test
```
pytest test/test_lotto_generator.py
```

## Develope Environment
- MacOS(M2)
- VSCode
- miniconda
- python 3.13

## Project Structure
```
lotto_predictor/
|- .gitignore
|- README.md
|- main.py
|- src/
    |- lotto_generator.py
|- test/
    |- test_lotto_generator.py
```
- .gitignore: 업로드 하지 않을 파일 및 디렉터리 목록
- README.md: 
- main.py: 실행 파일
- src/lotto_generator.py: 난수 랜덤 모듈
- test/test_lotto_generator.py: 난수 랜덤 모듈 테스트 코드
