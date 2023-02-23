""" This code is meant to be compiled to a standalone executable by PyInstaller
    It will display a UI that allows the user to determine if they want to install virtualbox or not.
"""
from functools import cache
from enum import Enum
from pathlib import Path
import shutil
import platform
import subprocess

from PySide2.QtWidgets import QMessageBox

import application


def main() -> None:
    application.show_window()


if __name__ == '__main__':
    main()
