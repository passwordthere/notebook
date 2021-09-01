import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()               #界面绘制交给initUI

    def initUI(self):
        self.setGeometry(300,300,300,220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)    #创建应用对象；sys.argv是一个list，从命令行输入参数
    ex = Example()
    sys.exit(app.exec_())