# -*- coding: utf-8 -*-
import sys
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from updown_project.app import UpDownApp


if __name__ == "__main__":
    app = UpDownApp()
    app.run()
