import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog
import logging
import zipfile

# 配置日志
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'ZIP文件名导出器'
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(100, 100, 800, 600)  # 设置窗口初始位置和大小

        layout = QVBoxLayout(self)
        self.folder_label = QLabel('文件夹路径:', self)
        self.folder_label.setStyleSheet('font-size: 16px; color: #333;')
        layout.addWidget(self.folder_label)
        self.folder_entry = QLineEdit(self)
        self.folder_entry.setStyleSheet('font-size: 14px; padding: 15px; border: 1px solid #ccc; border-radius: 5px;')
        self.folder_entry.setMinimumHeight(50)  # 设置文本框最小高度
        layout.addWidget(self.folder_entry)
        self.browse_button = QPushButton('选择文件夹', self)
        self.browse_button.setStyleSheet('font-size: 14px; padding: 15px; background-color: #007bff; color: #fff; border: none; border-radius: 5px;')
        self.browse_button.clicked.connect(self.selectFolder)
        layout.addWidget(self.browse_button)
        self.start_button = QPushButton('开始', self)
        self.start_button.setStyleSheet('font-size: 14px; padding: 15px; background-color: #28a745; color: #fff; border: none; border-radius: 5px;')
        self.start_button.clicked.connect(self.generateFile)
        layout.addWidget(self.start_button)
class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'ZIP文件名导出器'
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        layout = QVBoxLayout(self)
        self.folder_label = QLabel('文件夹路径:', self)
        layout.addWidget(self.folder_label)
        self.folder_entry = QLineEdit(self)
        layout.addWidget(self.folder_entry)
        self.browse_button = QPushButton('选择文件夹', self)
        self.browse_button.clicked.connect(self.selectFolder)
        layout.addWidget(self.browse_button)
        self.start_button = QPushButton('开始', self)
        self.start_button.clicked.connect(self.generateFile)
        layout.addWidget(self.start_button)

    def selectFolder(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        folder_path, _ = QFileDialog.getOpenFileName(self, "选择文件夹", "", "ZIP Files (*.zip)", options=options)
        if folder_path:
            self.folder_entry.setText(folder_path)

    def generateFile(self):
        folder_path = self.folder_entry.text()

        # 输出日志信息
        logging.info(f'开始生成文件：{folder_path}')

        try:
            # 解压ZIP文件
            output_folder = 'F:\飞书'  # 替换为你想要的目标文件夹路径
            with zipfile.ZipFile(folder_path, 'r') as zip_ref:
                zip_ref.extractall(os.path.join(output_folder, 'extracted_files'))
                logging.info(f'ZIP文件解压成功，已放置在目标文件夹：{output_folder}/extracted_files')
        except Exception as e:
            logging.error(f'解压ZIP文件时出错：{e}')

    def initUI(self):
        self.setWindowTitle(self.title)
        layout = QVBoxLayout(self)
        self.folder_label = QLabel('文件夹路径:', self)
        self.folder_label.setStyleSheet('font-size: 16px; color: #333;')
        layout.addWidget(self.folder_label)
        self.folder_entry = QLineEdit(self)
        self.folder_entry.setStyleSheet('font-size: 14px; padding: 10px; border: 1px solid #ccc; border-radius: 5px;')
        self.folder_entry.setMinimumHeight(40)  # 设置文本框最小高度
        layout.addWidget(self.folder_entry)
        self.browse_button = QPushButton('选择文件夹', self)
        self.browse_button.setStyleSheet(
            'font-size: 14px; padding: 10px; background-color: #007bff; color: #fff; border: none; border-radius: 5px;')
        self.browse_button.clicked.connect(self.selectFolder)
        layout.addWidget(self.browse_button)
        self.start_button = QPushButton('开始', self)
        self.start_button.setStyleSheet(
            'font-size: 14px; padding: 10px; background-color: #28a745; color: #fff; border: none; border-radius: 5px;')
        self.start_button.clicked.connect(self.generateFile)
        layout.addWidget(self.start_button)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())