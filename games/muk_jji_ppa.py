# -*- coding: utf-8 -*-
import random
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
RESULT_FILE = DATA_DIR / "muk_jji_ppa_result.txt"

CHOICES = ["묵", "찌", "빠"]


def save_result(result):
    DATA_DIR.mkdir(exist_ok=True)

    with open(RESULT_FILE, "a", encoding="utf-8") as file:
        file.write(result + "\n")


def get_winner(user, computer):
    if user == computer:
        return "draw"

    if user == "묵" and computer == "찌":
        return "user"
    if user == "찌" and computer == "빠":
        return "user"
    if user == "빠" and computer == "묵":
        return "user"

    return "computer"


def play_muk_jji_ppa():
    print("\n[묵찌빠 게임]")
    print("묵, 찌, 빠 중 하나를 입력하세요.")
    print("끝내려면 q를 입력하세요.")

    while True:
        user = input("입력: ").strip()

        if user.lower() == "q":
            print("묵찌빠 게임을 종료합니다.")
            break

        if user not in CHOICES:
            print("묵, 찌, 빠 중에서 입력해주세요.")
            continue

        computer = random.choice(CHOICES)
        winner = get_winner(user, computer)

        print(f"나: {user}")
        print(f"컴퓨터: {computer}")

        if winner == "draw":
            print("비겼습니다.")
            save_result("무승부")
        elif winner == "user":
            print("이겼습니다!")
            save_result("승리")
        else:
            print("졌습니다.")
            save_result("패배")
