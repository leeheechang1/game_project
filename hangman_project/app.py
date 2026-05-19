# -*- coding: utf-8 -*-
from pathlib import Path

from .hangman_game import HangmanGame
from .ranking_board import RankingBoard


class HangmanApp:
    def __init__(self):
        self.project_dir = Path(__file__).resolve().parent
        self.data_dir = self.project_dir / "data"
        self.ranking_board = RankingBoard(self.data_dir / "result.txt")
        self.game = HangmanGame(self.data_dir / "words.txt")

    def show_menu(self):
        print("\n[행맨 프로젝트]")
        print("1. 게임 시작")
        print("2. 결과 보기")
        print("0. 뒤로 가기")

    def run(self):
        while True:
            self.show_menu()
            choice = input("메뉴 선택: ").strip()

            if choice == "1":
                result = self.game.play()
                if result is not None:
                    self.ranking_board.save_result(result)
            elif choice == "2":
                self.ranking_board.show()
            elif choice == "0":
                break
            else:
                print("메뉴 번호를 다시 입력해주세요.")
