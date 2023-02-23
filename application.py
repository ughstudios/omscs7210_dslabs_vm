import sys
from pathlib import Path
import threading

from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QWidget, QLineEdit, QFileDialog

from vbox import get_vbox_manager


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Distributed Systems QuickStarter')
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        self.vbox = QVBoxLayout()
        self.main_widget.setLayout(self.vbox)

        instruction_lines = ['The purpose of this tool is to import a virtual machine template and import it into virtualbox.']
        self.instructions = QLabel('\n'.join(instruction_lines))
        self.vbox.addWidget(self.instructions)

        self.hbox = QHBoxLayout()
        self.path = QLineEdit()
        self.vbox_path_label = QLabel('Path to vbox executable (only change if unset): ')
        self.vbox_path_label.setToolTip('Browse to the correct path of your vboxmanager executable.')
        self.browse_button = QPushButton('Browse')
        self.browse_button.clicked.connect(self.on_browse_clicked)

        self.hbox.addWidget(self.vbox_path_label)
        self.hbox.addWidget(self.path)
        self.hbox.addWidget(self.browse_button)
        self.vbox.addLayout(self.hbox)

        self.start_button = QPushButton('Start Import')
        self.start_button.clicked.connect(self.on_start_import_clicked)

        self.vbox.addWidget(self.start_button)
        self.find_vboxmanager_exe()

    def on_start_import_clicked(self) -> None:
        # if we wanted to improve this could just make a browse button to browse for the template.
        template_path = Path.cwd() / 'template' / 'distributed_systems_template.ova'
        self.import_thread = threading.Thread(target=get_vbox_manager().import_template, args=(template_path, self.start_button, self.progress_label))
        self.import_thread.start()
        self.start_button.setEnabled(False)

    def find_vboxmanager_exe(self) -> None:
        manager = get_vbox_manager()
        if manager.vboxmanage.exists():
            self.path.setText(str(manager.vboxmanage))

    def on_browse_clicked(self) -> None:
        exe, _ = QFileDialog.getOpenFileName(None, 'VirtualBoxManager Executable')
        self.path.setText(exe)


def show_window() -> None:
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    app.exec_()
