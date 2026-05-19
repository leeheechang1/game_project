# -*- coding: utf-8 -*-
from pathlib import Path

from hangman_project.app import HangmanApp
from mukjjippa_project.app import MukJjiPpaApp
from updown_project.app import UpDownApp


class GameLauncher:
    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.apps = {
            "1": ("업앤다운 게임", UpDownApp()),
            "2": ("행맨 게임", HangmanApp()),
            "3": ("묵찌빠 게임", MukJjiPpaApp()),
        }

    def show_menu(self):
        print("\n===== 게임 모음 =====")
        print("1. 업앤다운 게임")
        print("2. 행맨 게임")
        print("3. 묵찌빠 게임")
        print("0. 종료")

    def run(self):
        while True:
            self.show_menu()
            choice = input("실행할 게임 번호: ").strip()

            if choice == "0":
                print("프로그램을 종료합니다.")
                break

            if choice not in self.apps:
                print("메뉴 번호를 다시 입력해주세요.")
                continue

            game_name, app = self.apps[choice]
            print(f"\n{game_name}을 시작합니다.")
            app.run()


if __name__ == "__main__":
    launcher = GameLauncher()
    launcher.run()
