from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap
from monte_carlo import *
from func_from_input import *
import sys
from math import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Площадь под графиком')

        self.label = QLabel('')

        self.input = QLineEdit()
        self.input1 = QLineEdit()
        self.input2 = QLineEdit()
        self.ready_button = QPushButton('Вычислить')
        self.ready_button.clicked.connect(self.ready)
        self.pic = QLabel()
        self.pic = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.input1)
        layout.addWidget(self.input2)
        layout.addWidget(self.ready_button)
        layout.addWidget(self.label)
        '''layout.addWidget(self.label1)'''

        captions = QVBoxLayout()
        captions.addWidget(QLabel("введите ф-ю"))
        captions.addWidget(QLabel("введите начало промежутка"))
        captions.addWidget(QLabel("введите конец промежутка"))
        captions.addWidget(QLabel("вывод метод Монте Карло: "))
        '''captions.addWidget(QLabel("вывод апроксимация параболлой: "))'''

        final = QHBoxLayout()
        final.addLayout(captions)
        final.addLayout(layout)

        final_final = QVBoxLayout()
        final_final.addLayout(final)
        final_final.addWidget(self.pic)

        container = QWidget()
        container.setLayout(final_final)

        self.setCentralWidget(container)

    def ready(self):
        funcs = func_from_in(self.input.text())
        print(funcs)
        f, func = funcs[0], funcs[1]
        count = 10000000
        scope_of_values = gr_and_leas(func, extr(f), int(self.input1.text()), int(self.input2.text()))
        greatest, least = scope_of_values[0], scope_of_values[1]
        s_func_by_mc = s_monte_carlo(func, int(self.input1.text()), int(self.input2.text()), greatest, least, count)
        '''bbo = approx_par(int(self.input1.text()), int(self.input2.text()), self.input.text())'''
        self.label.setText(str(s_func_by_mc))
        '''self.label1.setText(str(bbo))'''
        show_s_by_func(func, int(self.input1.text()), int(self.input2.text()), 0)
        self.pic.setPixmap(QPixmap("saved_figure.png"))


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()


if __name__ == "__main__":
    main()
