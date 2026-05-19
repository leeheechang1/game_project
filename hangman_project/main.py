# -*- coding: utf-8 -*-
import sys
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from hangman_project.app import HangmanApp


if __name__ == "__main__":
    app = HangmanApp()
    app.run()
