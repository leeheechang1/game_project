# -*- coding: utf-8 -*-
import random
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
WORD_FILE = DATA_DIR / "hangman_words.txt"
RESULT_FILE = DATA_DIR / "hangman_result.txt"


DEFAULT_WORDS = ["python", "school", "game", "computer", "banana"]


def prepare_word_file():
    DATA_DIR.mkdir(exist_ok=True)

    if WORD_FILE.exists():
        return

    with open(WORD_FILE, "w", encoding="utf-8") as file:
        for word in DEFAULT_WORDS:
            file.write(word + "\n")


def load_words():
    prepare_word_file()

    with open(WORD_FILE, "r", encoding="utf-8") as file:
        words = [line.strip() for line in file if line.strip()]

    return words


def save_result(result, answer):
    with open(RESULT_FILE, "a", encoding="utf-8") as file:
        file.write(f"{result}: 정답은 {answer}\n")


def play_hangman():
    words = load_words()
    answer = random.choice(words)
    guessed_letters = []
    life = 6

    print("\n[행맨 게임]")
    print("영어 단어의 알파벳을 하나씩 맞혀보세요.")
    print("끝내려면 q를 입력하세요.")

    while life > 0:
        display = ""
        for letter in answer:
            if letter in guessed_letters:
                display += letter + " "
            else:
                display += "_ "

        print(f"\n단어: {display}")
        print(f"남은 기회: {life}")
        print(f"입력한 글자: {', '.join(guessed_letters) if guessed_letters else '없음'}")

        if "_" not in display:
            print(f"성공! 정답은 {answer}입니다.")
            save_result("성공", answer)
            return

        guess = input("알파벳 입력: ").strip().lower()

        if guess == "q":
            print("행맨 게임을 종료합니다.")
            return

        if len(guess) != 1 or not guess.isalpha():
            print("알파벳 한 글자만 입력해주세요.")
            continue

        if guess in guessed_letters:
            print("이미 입력한 글자입니다.")
            continue

        guessed_letters.append(guess)

        if guess not in answer:
            life -= 1
            print("틀렸습니다.")
        else:
            print("맞았습니다.")

    print(f"실패! 정답은 {answer}였습니다.")
    save_result("실패", answer)
