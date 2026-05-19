# -*- coding: utf-8 -*-
import random


class UpDownGame:
    def __init__(self, start=1, end=100):
        self.start = start
        self.end = end
        self.answer = random.randint(self.start, self.end)
        self.try_count = 0

    def reset(self):
        self.answer = random.randint(self.start, self.end)
        self.try_count = 0

    def play(self):
        self.reset()
        print("\n[업앤다운 게임]")
        print(f"{self.start}부터 {self.end} 사이의 숫자를 맞혀보세요.")
        print("끝내려면 q를 입력하세요.")

        while True:
            user_input = input("숫자 입력: ").strip()

            if user_input.lower() == "q":
                print("게임을 종료합니다.")
                return None

            if not user_input.isdigit():
                print("숫자만 입력해주세요.")
                continue

            guess = int(user_input)

            if guess < self.start or guess > self.end:
                print(f"{self.start}부터 {self.end} 사이의 숫자를 입력해주세요.")
                continue

            self.try_count += 1

            if guess < self.answer:
                print("업! 더 큰 숫자입니다.")
            elif guess > self.answer:
                print("다운! 더 작은 숫자입니다.")
            else:
                print(f"정답입니다! {self.try_count}번 만에 맞혔어요.")
                return self.try_count
