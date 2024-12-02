import os
import sys
import random
import string
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QPushButton, QListWidget,
    QCheckBox, QLineEdit, QLabel, QMenuBar, QAction, QMessageBox
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

def resource_path(relative_path):
        """获取程序中所需文件资源的绝对路径"""
        try:
        # PyInstaller创建临时文件夹,将路径存储于_MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

class PasswordGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("密码生成器")
        self.setGeometry(100, 100, 350, 280)  # 增加窗口宽度以容纳图片
        self.initUI()

    def initUI(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # 勾选包含项目标签
        self.label_2 = QLabel("勾选包含项目", central_widget)
        self.label_2.setGeometry(10, 10, 100, 15)

        # 输入位数标签
        self.label_3 = QLabel("输入位数", central_widget)
        self.label_3.setGeometry(150, 10, 100, 15)

        # 大写字母复选框和输入框
        self.checkBox = QCheckBox("大写字母", central_widget)
        self.checkBox.setGeometry(10, 30, 100, 21)
        self.lineEdit_1 = QLineEdit(central_widget)
        self.lineEdit_1.setGeometry(150, 30, 61, 23)

        # 小写字母复选框和输入框
        self.checkBox_2 = QCheckBox("小写字母", central_widget)
        self.checkBox_2.setGeometry(10, 60, 100, 21)
        self.lineEdit_2 = QLineEdit(central_widget)
        self.lineEdit_2.setGeometry(150, 60, 61, 23)

        # 数字复选框和输入框
        self.checkBox_3 = QCheckBox("数字", central_widget)
        self.checkBox_3.setGeometry(10, 90, 100, 21)
        self.lineEdit_3 = QLineEdit(central_widget)
        self.lineEdit_3.setGeometry(150, 90, 61, 23)

        # 特殊字符复选框和输入框
        self.checkBox_4 = QCheckBox("特殊字符", central_widget)
        self.checkBox_4.setGeometry(10, 120, 100, 21)
        self.lineEdit_4 = QLineEdit(central_widget)
        self.lineEdit_4.setGeometry(150, 120, 61, 23)

        # 生成按钮
        self.pushButton = QPushButton("生成", central_widget)
        self.pushButton.setGeometry(10, 160, 71, 41)
        self.pushButton.clicked.connect(self.generate_password)

        # 复制结果按钮
        self.pushButton_2 = QPushButton("复制结果", central_widget)
        self.pushButton_2.setGeometry(100, 160, 91, 41)
        self.pushButton_2.clicked.connect(self.copy_result)

        # 列表框
        self.listWidget = QListWidget(central_widget)
        self.listWidget.setGeometry(10, 210, 330, 40)

        # 菜单栏
        menubar = self.menuBar()
        help_menu = menubar.addMenu("帮助")
        help_action = QAction("不会用就来问我捏", self)
        help_menu.addAction(help_action)

        # 添加图片标签
        self.image_label = QLabel(central_widget)
        self.image_label.setGeometry(210, 10, 160, 200)  # 根据窗口大小调整位置和尺寸
        self.image_label.setAlignment(Qt.AlignCenter)

        # 加载并设置图片
        pixmap = QPixmap(resource_path(("老婆可爱捏.png"))) 
        if pixmap.isNull():
            QMessageBox.warning(self, "图片加载错误", "无法加载指定的图片。请检查图片路径。")
        else:
            self.image_label.setPixmap(pixmap.scaled(
                self.image_label.width(),
                self.image_label.height(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            ))

    def generate_password(self):
        characters = ""
        lengths = []

        # 清空列表框
        self.listWidget.clear()

        if self.checkBox.isChecked():
            try:
                length = int(self.lineEdit_1.text())
                if length < 0:
                    raise ValueError
                characters += string.ascii_uppercase
                lengths.append((string.ascii_uppercase, length))
            except ValueError:
                QMessageBox.warning(self, "输入错误", "请输入有效的正整数位数（大写字母）。")
                return

        if self.checkBox_2.isChecked():
            try:
                length = int(self.lineEdit_2.text())
                if length < 0:
                    raise ValueError
                characters += string.ascii_lowercase
                lengths.append((string.ascii_lowercase, length))
            except ValueError:
                QMessageBox.warning(self, "输入错误", "请输入有效的正整数位数（小写字母）。")
                return

        if self.checkBox_3.isChecked():
            try:
                length = int(self.lineEdit_3.text())
                if length < 0:
                    raise ValueError
                characters += string.digits
                lengths.append((string.digits, length))
            except ValueError:
                QMessageBox.warning(self, "输入错误", "请输入有效的正整数位数（数字）。")
                return

        if self.checkBox_4.isChecked():
            try:
                length = int(self.lineEdit_4.text())
                if length < 0:
                    raise ValueError
                characters += string.punctuation
                lengths.append((string.punctuation, length))
            except ValueError:
                QMessageBox.warning(self, "输入错误", "请输入有效的正整数位数（特殊字符）。")
                return

        if not characters:
            QMessageBox.warning(self, "选择错误", "请选择至少一种字符类型。")
            return

        # 生成密码
        password = ""
        for char_set, count in lengths:
            password += ''.join(random.choices(char_set, k=count))
        
        # 打乱密码字符顺序
        password = ''.join(random.sample(password, len(password)))

        self.listWidget.addItem(password)

    def copy_result(self):
        if self.listWidget.count() == 0:
            QMessageBox.warning(self, "复制错误", "没有生成的密码可以复制。")
            return
        password = self.listWidget.item(self.listWidget.count() - 1).text()
        clipboard = QApplication.clipboard()
        clipboard.setText(password)
        QMessageBox.information(self, "复制成功", "密码已复制到剪贴板。")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PasswordGenerator()
    window.show()
    sys.exit(app.exec_())
