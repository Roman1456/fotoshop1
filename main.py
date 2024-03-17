import json
import os

from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import *
from PIL import Image

app = QApplication([])

app.setStyleSheet("""
    QWidget
    {
    background-color: #0000ff;
    }



    QLabel
    {
        background-color: #fbffdb;
        font-size: 18px;
        border-style: double;
        border-width: 5px;
        border-color: orange;
        border-radius: 12px;
    }

    QListWidget
    {
        background-color: #fbffdb;
        border-style: double;
        border-width: 5px;
        border-color: orange;
        border-radius: 12px;
    }

   QTextEdit
   {
        background-color: #fbffdb;
        border-style: double;
        border-width: 5px;
        border-color: orange;
        border-radius: 12px;
   }

    QLineEdit
    {
        background-color: #fbffdb;
        border-style: double;
        border-width: 5px;
        border-color: orange;
        border-radius: 12px;
    }

    QPushButton 
    {  
        background-color: #e0f542;
        font-size: 18px;
        color: blue;
        border-style: double;
        border-width: 5px;
        border-color: orange;
        border-radius: 12px;
        min-height: 20px;
        min-width: 100;
        margin: 5px;
    }


""")

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



def pil2pixmap(im):
    if im.mode == "RGB":
        r, g, b = im.split()
        im = Image.merge("RGB", (b, g, r))
    elif im.mode == "RGBA":
        r, g, b, a = im.split()
        im = Image.merge("RGBA", (b, g, r, a))
    elif im.mode == "L":
        im = im.convert("RGBA")
    im2 = im.convert("RGBA")
    data = im2.tobytes("raw", "RGBA")
    qim = QImage(data, im.size[0], im.size[1], QImage.Format_ARGB32)
    pixmap = QPixmap.fromImage(qim)
    return pixmap


class Bublik:
    def __int__(self):
        self.image = None
        self.folder = None
        self.image_name = None

    def load(self):
        full_path = os.path.join(self.folder,self.image_name)
        self.image = Image.open(full_path)
    def show_image(self):
        pixel = pil2pixmap(self.image)
        qest_lbl.setPixmap(pixel)

bublik = Bublik()

def show_directory():
    bublik.folder = QFileDialog.getExistingDirectory()
    list_files = os.listdir(bublik.folder)
    answer_list.clear()
    for file in list_files:
        if file.endswith("png"):
             answer_list.addItem(file)

def show_foto():
    image_name =answer_list.currentItem().text()
    bublik.image_name = image_name
    bublik.load()
    bublik.show_image()

answer_list.currentRowChanged.connect(show_foto)
qest_btn.clicked.connect(show_directory)
window.show()
app.exec()