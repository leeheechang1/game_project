# -*- coding: utf-8 -*-


class RankingBoard:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_path.parent.mkdir(exist_ok=True)
        self.file_path.touch(exist_ok=True)

    def save_score(self, name, try_count):
        with open(self.file_path, "a", encoding="utf-8") as file:
            file.write(f"{name},{try_count}\n")

        print("랭킹이 저장되었습니다.")

    def load_scores(self):
        scores = []

        with open(self.file_path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                name, try_count = line.split(",")
                scores.append((name, int(try_count)))

        return sorted(scores, key=lambda score: score[1])

    def show(self):
        scores = self.load_scores()

        print("\n[업앤다운 랭킹]")
        if not scores:
            print("아직 저장된 랭킹이 없습니다.")
            return

        for rank, score in enumerate(scores[:5], start=1):
            name, try_count = score
            print(f"{rank}등. {name} - {try_count}번")
