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

mine_line = QHBoxLayout()
mine_line1= QHBoxLayout()

h1 = QVBoxLayout()
h1.addWidget(qest_btn)
h1.addWidget(answer_list)
mine_line.addLayout(h1)

v2 = QVBoxLayout()
v2.addWidget(qest_lbl)
h2 = QHBoxLayout()
h2.addWidget(qest_lbl)
h2.addLayout(mine_line1)
h2.addWidget(qest_btn1)
h2.addWidget(qest_btn2)
h2.addWidget(qest_btn3)
h2.addWidget(qest_btn4)
h2.addWidget(qest_btn5)
v2.addLayout(h2)
mine_line.addLayout(v2)

window.setLayout(mine_line)














window.show()
app.exec()