import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)    #创建应用对象；sys.argv是一个list，从命令行输入参数
    w = QWidget()                   #QWidget是pyqt5所有用户界面对象的基类；提供默认构造函数，且默认构造函数没有父类
    w.resize(600, 500)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()
    
    sys.exit(app.exec_())