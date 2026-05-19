# -*- coding: utf-8 -*-
import random


class MukJjiPpaGame:
    def __init__(self):
        self.choices = ["가위", "바위", "보"]
        self.attackers = {
            "user": "사용자",
            "computer": "컴퓨터",
        }

    def get_rock_scissors_paper_winner(self, user, computer):
        if user == computer:
            return "draw"

        if user == "가위" and computer == "보":
            return "user"
        if user == "바위" and computer == "가위":
            return "user"
        if user == "보" and computer == "바위":
            return "user"

        return "computer"

    def decide_first_attacker(self):
        print("\n먼저 가위바위보로 공격 순서를 정합니다.")

        while True:
            user = input("가위, 바위, 보 중 입력: ").strip()

            if user == "0":
                print("게임을 종료합니다.")
                return None

            if user not in self.choices:
                print("가위, 바위, 보 중에서 입력해주세요.")
                continue

            computer = random.choice(self.choices)
            winner = self.get_rock_scissors_paper_winner(user, computer)

            print(f"나: {user}")
            print(f"컴퓨터: {computer}")

            if winner == "draw":
                print("비겼습니다. 다시 정합니다.")
                continue

            print(f"{self.attackers[winner]}가 먼저 공격합니다.")
            return winner

    def play_muk_jji_ppa_turn(self, attacker):
        print("\n이제 묵찌빠를 시작합니다.")
        print("같은 것을 내면 공격자가 이깁니다.")

        while True:
            print(f"\n현재 공격자: {self.attackers[attacker]}")
            user = input("가위, 바위, 보 중 입력: ").strip()

            if user == "0":
                print("게임을 종료합니다.")
                return None

            if user not in self.choices:
                print("가위, 바위, 보 중에서 입력해주세요.")
                continue

            computer = random.choice(self.choices)
            print(f"나: {user}")
            print(f"컴퓨터: {computer}")

            if user == computer:
                if attacker == "user":
                    print("승리! 같은 것을 냈고 내가 공격자입니다.")
                    return "승리"

                print("패배! 같은 것을 냈고 컴퓨터가 공격자입니다.")
                return "패배"

            attacker = self.get_rock_scissors_paper_winner(user, computer)
            print(f"공격자가 {self.attackers[attacker]}로 바뀝니다.")

    def play(self):
        print("\n[묵찌빠 게임]")
        print("0을 입력하면 종료합니다.")

        attacker = self.decide_first_attacker()
        if attacker is None:
            return None

        return self.play_muk_jji_ppa_turn(attacker)
