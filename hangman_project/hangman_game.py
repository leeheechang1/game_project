# -*- coding: utf-8 -*-
import random


class HangmanGame:
    def __init__(self, word_file_path):
        self.word_file_path = word_file_path
        self.default_words = [
            "apple", "angle", "beach", "bread", "brain", "brick", "brush", "candy", "chair", "charm",
            "chess", "cloud", "cream", "dance", "dream", "drink", "earth", "eagle", "faith", "field",
            "flame", "floor", "focus", "fruit", "giant", "glass", "grape", "green", "heart", "honey",
            "horse", "house", "image", "jelly", "juice", "knife", "lemon", "light", "magic", "mango",
            "money", "month", "music", "night", "ocean", "olive", "paint", "paper", "party", "peach",
            "phone", "plant", "queen", "quick", "radio", "river", "robot", "round", "salad", "scale",
            "sheep", "shirt", "skirt", "sleep", "smart", "smile", "snake", "sound", "space", "spoon",
            "sport", "stone", "story", "sugar", "table", "tiger", "timer", "toast", "train", "truck",
            "uncle", "union", "video", "voice", "water", "whale", "wheel", "white", "world", "youth",
            "zebra", "alarm", "badge", "basic", "black", "brown", "crown", "diary", "happy", "prize",
        ]
        self.life = 6
        self.answer = ""
        self.guessed_letters = []
        self.prepare_word_file()

    def prepare_word_file(self):
        self.word_file_path.parent.mkdir(exist_ok=True)

        if self.word_file_path.exists():
            words = self.load_words()
            if len(words) == 100 and all(len(word) == 5 for word in words):
                return

        with open(self.word_file_path, "w", encoding="utf-8") as file:
            for word in self.default_words:
                file.write(word + "\n")

    def load_words(self):
        with open(self.word_file_path, "r", encoding="utf-8") as file:
            return [line.strip().lower() for line in file if line.strip()]

    def reset(self):
        words = self.load_words()
        self.answer = random.choice(words)
        self.life = 6
        self.guessed_letters = []

    def make_display_word(self):
        letters = []

        for letter in self.answer:
            if letter in self.guessed_letters:
                letters.append(letter)
            else:
                letters.append("_")

        return " ".join(letters)

    def play(self):
        self.reset()
        print("\n[행맨 게임]")
        print("5글자 영어 단어의 알파벳을 하나씩 맞혀보세요.")
        print("끝내려면 0을 입력하세요.")

        while self.life > 0:
            display_word = self.make_display_word()
            print(f"\n단어: {display_word}")
            print(f"남은 기회: {self.life}")

            if "_" not in display_word:
                print(f"성공! 정답은 {self.answer}입니다.")
                return f"성공,{self.answer}"

            guess = input("알파벳 입력: ").strip().lower()

            if guess == "0":
                print("게임을 종료합니다.")
                return None

            if len(guess) != 1 or not guess.isalpha():
                print("알파벳 한 글자만 입력해주세요.")
                continue

            if guess in self.guessed_letters:
                print("이미 입력한 글자입니다.")
                continue

            self.guessed_letters.append(guess)

            if guess in self.answer:
                print("맞았습니다.")
            else:
                self.life -= 1
                print("틀렸습니다.")

        print(f"실패! 정답은 {self.answer}였습니다.")
        return f"실패,{self.answer}"
