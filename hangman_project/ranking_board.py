# -*- coding: utf-8 -*-


class RankingBoard:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_path.parent.mkdir(exist_ok=True)
        self.file_path.touch(exist_ok=True)

    def save_result(self, result):
        with open(self.file_path, "a", encoding="utf-8") as file:
            file.write(result + "\n")

        print("결과가 저장되었습니다.")

    def show(self):
        print("\n[행맨 결과]")

        with open(self.file_path, "r", encoding="utf-8") as file:
            results = [line.strip() for line in file if line.strip()]

        if not results:
            print("아직 저장된 결과가 없습니다.")
            return

        for number, result in enumerate(results, start=1):
            status, answer = result.split(",")
            print(f"{number}. {status} - 정답: {answer}")
