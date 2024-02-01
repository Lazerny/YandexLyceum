from PyQt5 import QtCore

from second import show_map

import os
import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

SCREEN_SIZE = [600, 450]


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, *SCREEN_SIZE)
        self.setWindowTitle('Отображение карты')

        self.ll = [37.530887, 55.703118]
        self.getImage()
        self.showMap()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key.Key_Left:
            self.ll[0] -= self.ll[0] * 0.00001
            self.getImage()
            self.showMap()
            pass
        elif event.key() == QtCore.Qt.Key.Key_Right:
            self.ll[0] += self.ll[0] * 0.00001
            self.getImage()
            self.showMap()
            pass
        elif event.key() == QtCore.Qt.Key.Key_Up:
            self.ll[1] += self.ll[1] * 0.00001
            self.getImage()
            self.showMap()
            pass
        elif event.key() == QtCore.Qt.Key.Key_Down:
            self.ll[1] -= self.ll[1] * 0.00001
            self.getImage()
            self.showMap()
            pass

    def getImage(self):
        response = show_map(ll=','.join(list(map(str, self.ll))))

        self.map_file = "map.png"
        with open(self.map_file, "wb") as file:
            file.write(response)

    def showMap(self):
        self.pixmap = QPixmap(self.map_file)
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(600, 450)
        self.image.setPixmap(self.pixmap)
        self.image.show()
        self.image.update()

    def closeEvent(self, event):
        os.remove(self.map_file)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
