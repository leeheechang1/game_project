# -*- coding: utf-8 -*-
import random
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
SCORE_FILE = DATA_DIR / "up_down_score.txt"


def save_score(count):
    DATA_DIR.mkdir(exist_ok=True)

    with open(SCORE_FILE, "a", encoding="utf-8") as file:
        file.write(f"{count}번 만에 정답\n")


def show_scores():
    if not SCORE_FILE.exists():
        print("아직 저장된 점수가 없습니다.")
        return

    print("\n[업앤다운 기록]")
    with open(SCORE_FILE, "r", encoding="utf-8") as file:
        print(file.read().strip())


def play_up_down():
    answer = random.randint(1, 100)
    count = 0

    print("\n[업앤다운 게임]")
    print("1부터 100 사이의 숫자를 맞혀보세요.")
    print("끝내려면 q를 입력하세요.")

    while True:
        user_input = input("숫자 입력: ").strip()

        if user_input.lower() == "q":
            print("업앤다운 게임을 종료합니다.")
            break

        if not user_input.isdigit():
            print("숫자만 입력해주세요.")
            continue

        guess = int(user_input)

        if guess < 1 or guess > 100:
            print("1부터 100 사이의 숫자를 입력해주세요.")
            continue

        count += 1

        if guess < answer:
            print("업! 더 큰 숫자입니다.")
        elif guess > answer:
            print("다운! 더 작은 숫자입니다.")
        else:
            print(f"정답입니다! {count}번 만에 맞혔어요.")
            save_score(count)
            show_scores()
            break
