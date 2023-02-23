""" Contains helper functions for interacting with virtual box """
import sys
from enum import Enum
from functools import cache
import shutil
from pathlib import Path
import subprocess
import threading

from qtutils import inmain_later

from PySide2.QtWidgets import QMessageBox, QPushButton, QLabel


class VBoxManager:
    def __init__(self):
        self.vboxmanage = Path(str(shutil.which('vboxmanage')))
        if not self.vboxmanage:
            # This doesn't appear to work on mac. :(
            mbox = QMessageBox(None, 'VBoxManager', 'Could not find the location of virtualbox. Is it installed?')
            mbox.show()
            sys.exit(mbox.exec_())

    def import_template(self, path_to_template: Path, start_button: QPushButton, progress_label: QLabel) -> None:
        if threading.currentThread().name == 'MainThread':
            raise Exception('Do not call this from the main thread.')

        cmdline = [str(self.vboxmanage), 'import', str(path_to_template)]
        subprocess.check_output(cmdline, stdout=subprocess.PIPE)  # type: ignore
        inmain_later(start_button.setEnabled, False)


@cache
def get_vbox_manager() -> VBoxManager:
    return VBoxManager()
