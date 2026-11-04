 # 가위 바위 보 게임 미니 프로젝트

import random

# 스코어 변수는 반복문(while) 바깥에 있어야 게임이 끝나도 점수가 유지/누적 됩니다!
my_score = 0
com_score = 0

while True:
    print("=" * 40)
    print("　　　　가위 / 바위 / 보 게임")
    print("=" * 40)
    print("1. 가위 / 2. 바위 / 3. 보")

    # 1. 사용자 입력 받기
    user_input = int(input("번호를 선택하세요. : "))

    # 2. 컴퓨터 난수 생성 (1~3)
    com_input = random.randint(1, 3)

    # 3. 사용자의 숫자(1, 2, 3)를 문자로 변환
    if user_input == 1:
        my_choice = "가위"
    elif user_input == 2:
        my_choice = "바위"
    elif user_input == 3:
        my_choice = "보"

    # 4. 컴퓨터의 숫자(1, 2, 3)를 문자로 변환
    if com_input == 1:
        com_choice = "가위"
    elif com_input == 2:
        com_choice = "바위"
    elif com_input == 3:
        com_choice = "보"

    # 5. [게임 결과] 출력 포맷 (vs와 컴퓨터 이름 포함)
    print("\n[게임 결과]")
    print(f"나: {my_choice} vs {com_choice}")

    # 6. 승패 판정 및 스코어 계산 조건문
    if user_input == com_input:
        print("=> 비김")
    elif (
        (user_input == 1 and com_input == 3)
        or (user_input == 2 and com_input == 1)
        or (user_input == 3 and com_input == 2)
    ):
        print("=> 승리")
        my_score += 1 # 내 점수 1점 증가
    else:
        print("=> 패배")
        com_score += 1 # 컴퓨터 점수 1점 증가

    # 7. 현재 스코어 출력문 추가
    print(f"현재 스코어  나 {my_choice} : {com_score} 컴퓨터\n")

    # 8. 다시 도전 (yes/no) 입력값 검증 및 탈출 로직
    retry = input("다시 도전 (yes/no) : ")
    if retry == "no":
        print("게임을 종료합니다.")
        break
    print("-" * 30)