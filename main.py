from PyQt5.QtWidgets import *

app = QApplication([])

window = QWidget()
window.resize(700,500)

qest_btn = QPushButton("Папка")
qest_btn1 = QPushButton("Вліво")
qest_btn2 = QPushButton("Вправо")
qest_btn3 = QPushButton("Дзеркально")
qest_btn4 = QPushButton("Різкість")
qest_btn5 = QPushButton("Ч/Б")

qest_lbl = QLabel()

answer_list = QListWidget()





















window.show()
app.exec()