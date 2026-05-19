# 게임 모음 프로젝트

경로와 파일 입출력을 연습하기 위한 콘솔 게임 프로젝트입니다.

## 실행 방법

전체 게임 메뉴를 실행하려면 아래 명령어를 사용합니다.

```powershell
python .\main.py
```

각 게임만 따로 실행할 수도 있습니다.

```powershell
python .\updown_project\main.py
python .\hangman_project\main.py
python .\mukjjippa_project\main.py
```

## 폴더 구조

```text
updown_project/
├── main.py
├── updown_game.py
├── ranking_board.py
└── app.py

hangman_project/
├── main.py
├── hangman_game.py
├── ranking_board.py
└── app.py

mukjjippa_project/
├── main.py
├── mukjjippa_game.py
├── ranking_board.py
└── app.py
```

## 파일 역할

- `main.py`: 프로그램을 시작하는 파일입니다.
- `app.py`: 메뉴를 보여주고 게임과 랭킹판을 연결합니다.
- `*_game.py`: 실제 게임 규칙이 들어있는 클래스 파일입니다.
- `ranking_board.py`: 결과를 파일에 저장하고 다시 읽어오는 클래스 파일입니다.
- `data/`: 게임을 실행하면 자동으로 만들어지는 저장 폴더입니다.

## 수업 포인트

- `Path(__file__).resolve().parent`로 현재 파일의 폴더 경로를 구합니다.
- `mkdir(exist_ok=True)`로 저장 폴더를 만듭니다.
- `open(..., "w")`로 파일을 처음 저장합니다.
- `open(..., "a")`로 파일 끝에 결과를 추가합니다.
- `open(..., "r")`로 저장된 내용을 읽습니다.
