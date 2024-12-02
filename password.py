import sys
import random
import string
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QPushButton, QListWidget,
    QCheckBox, QLineEdit, QLabel, QMenuBar, QAction, QMessageBox
)

class PasswordGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("密码生成器")
        self.setGeometry(100, 100, 300, 280)
        self.initUI()

    def initUI(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # 勾选包含项目标签
        self.label_2 = QLabel("勾选包含项目", central_widget)
        self.label_2.setGeometry(10, 10, 91, 15)

        # 输入位数标签
        self.label_3 = QLabel("输入位数", central_widget)
        self.label_3.setGeometry(110, 10, 91, 15)

        # 大写字母复选框和输入框
        self.checkBox = QCheckBox("大写字母", central_widget)
        self.checkBox.setGeometry(10, 30, 93, 21)
        self.lineEdit_1 = QLineEdit(central_widget)
        self.lineEdit_1.setGeometry(110, 30, 61, 23)

        # 小写字母复选框和输入框
        self.checkBox_2 = QCheckBox("小写字母", central_widget)
        self.checkBox_2.setGeometry(10, 60, 93, 21)
        self.lineEdit_2 = QLineEdit(central_widget)
        self.lineEdit_2.setGeometry(110, 60, 61, 23)

        # 数字复选框和输入框
        self.checkBox_3 = QCheckBox("数字", central_widget)
        self.checkBox_3.setGeometry(10, 90, 93, 21)
        self.lineEdit_3 = QLineEdit(central_widget)
        self.lineEdit_3.setGeometry(110, 90, 61, 23)

        # 特殊字符复选框和输入框
        self.checkBox_4 = QCheckBox("特殊字符", central_widget)
        self.checkBox_4.setGeometry(10, 120, 93, 21)
        self.lineEdit_4 = QLineEdit(central_widget)
        self.lineEdit_4.setGeometry(110, 120, 61, 23)

        # 生成按钮
        self.pushButton = QPushButton("生成", central_widget)
        self.pushButton.setGeometry(10, 160, 71, 41)
        self.pushButton.clicked.connect(self.generate_password)

        # 复制结果按钮
        self.pushButton_2 = QPushButton("复制结果", central_widget)
        self.pushButton_2.setGeometry(105, 160, 71, 41)
        self.pushButton_2.clicked.connect(self.copy_result)

        # 列表框
        self.listWidget = QListWidget(central_widget)
        self.listWidget.setGeometry(0, 210, 300, 50)

        # 菜单栏
        menubar = self.menuBar()
        help_menu = menubar.addMenu("帮助")
        help_action = QAction("不会用就来问我捏", self)
        help_menu.addAction(help_action)

    def generate_password(self):
        characters = ""
        lengths = []

        # 清空列表框
        self.listWidget.clear()

        if self.checkBox.isChecked():
            try:
                length = int(self.lineEdit_1.text())
                characters += string.ascii_uppercase
                lengths.append((string.ascii_uppercase, length))
            except ValueError:
                QMessageBox.warning(self, "输入错误", "请输入有效的位数")
                return

        if self.checkBox_2.isChecked():
            try:
                length = int(self.lineEdit_2.text())
                characters += string.ascii_lowercase
                lengths.append((string.ascii_lowercase, length))
            except ValueError:
                QMessageBox.warning(self, "输入错误", "请输入有效的位数")
                return

        if self.checkBox_3.isChecked():
            try:
                length = int(self.lineEdit_3.text())
                characters += string.digits
                lengths.append((string.digits, length))
            except ValueError:
                QMessageBox.warning(self, "输入错误", "请输入有效的位数")
                return

        if self.checkBox_4.isChecked():
            try:
                length = int(self.lineEdit_4.text())
                characters += string.punctuation
                lengths.append((string.punctuation, length))
            except ValueError:
                QMessageBox.warning(self, "输入错误", "请输入有效的位数")
                return

        if not characters:
            QMessageBox.warning(self, "选择错误", "请选择至少一种字符类型")
            return

        password = []
        for char_type, length in lengths:
            password.extend(random.choices(char_type, k=length))

        random.shuffle(password)
        password = ''.join(password)
        self.listWidget.addItem(password)

    def copy_result(self):
        if self.listWidget.count() == 0:
            QMessageBox.information(self, "复制", "列表框中没有内容")
            return

        # 获取列表框中的第一项内容
        password = self.listWidget.item(0).text()
        clipboard = QApplication.clipboard()
        clipboard.setText(password)
        QMessageBox.information(self, "复制", "密码已复制到剪贴板")

def main():
    app = QApplication(sys.argv)
    window = PasswordGenerator()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()