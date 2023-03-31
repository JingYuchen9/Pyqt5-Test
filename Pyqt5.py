import sys
import numpy as np
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import random as random

x_Value_list = list()
y_Value_list = list()
x_Center_list = list()
y_Center_list = list()


class DrawAll(QWidget):

    def __init__(self):
        super(DrawAll, self).__init__()
        self.setWindowTitle("Ad Hoc Network")
        self.setGeometry(50, 50, 2500, 1400)

        self.color = QColor(0, 0, 255)
        self.x = 50
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_position)
        self.timer.start(50)

    def update_position(self):

        if self.x > 1800:
            self.x = 0
        if self.x <= 1800:
            self.x += 10

        self.update()

    def paintEvent(self, event):
        qp = QPainter(self)
        qp.setRenderHint(qp.Antialiasing)
        qp.begin(self)

        for x in range(10):
            x_value = x_Value_list[x]
            # print(x_value)
            y_value = y_Value_list[x]
            # print(y_value)
            hr = 300
            zr = hr
            circle = 360*16
            began = 0

            qp.setPen(QPen(QColor(random.randint(0, 255),
                                  random.randint(0, 255),
                                  random.randint(0, 255)), 5, Qt.SolidLine))
            qp.drawArc(x_value, y_value, hr, zr, began, circle)

            qp.setPen(QPen(QColor(random.randint(0, 255),
                                  random.randint(0, 255),
                                  random.randint(0, 255)), 30, Qt.SolidLine))
            qp.drawPoint(int(x_value+hr/2), int(y_value+zr/2))
            qp.setPen(QPen(QColor(0, 0, 0), 5, Qt.SolidLine))
            qp.drawText(int(x_value+hr/2), int(y_value+zr/2) - 40, f"{int(x_value+hr/2)}, {int(y_value+zr/2)}")
            x_Center_list.append(int(x_value+hr/2))
            y_Center_list.append(int(y_value+zr/2))
            # print("x = ", int(x_value+hr/2))
            # print("y = ", int(y_value+zr/2))
        drawline(qp)
        drawMoveCircle(self)

        # print("draw is called")
        qp.end()


def drawline(qp):
    # print("drawline is called")
    qp.setPen(QPen(QColor(0, 0, 0), 5, Qt.SolidLine))
    for start in range(10):
        for end in range(9):
            if(np.sqrt(np.square(x_Center_list[start] - x_Center_list[end]) +
                       np.square(y_Center_list[start] - y_Center_list[end])) <= 300):
                qp.drawLine(int(x_Center_list[start]),
                            int(y_Center_list[start]),
                            int(x_Center_list[end]),
                            int(y_Center_list[end]))


def drawMoveCircle(self):
    print("draw circle is called")
    painter = QPainter(self)
    painter.setRenderHint(QPainter.Antialiasing)
    painter.setPen(QPen(QColor(random.randint(0, 255),
                               random.randint(0, 255),
                               random.randint(0, 255)), 5, Qt.SolidLine))
    painter.setBrush(self.color)
    painter.drawArc(self.x, 600, 600, 600, 0, 360 * 16)

    painter.setPen(QPen(QColor(random.randint(0, 255),
                               random.randint(0, 255),
                               random.randint(0, 255)), 30, Qt.SolidLine))
    painter.drawPoint(int(self.x + 600 / 2), int(600 + 600 / 2))
    painter.setPen(QPen(QColor(0, 0, 0), 5, Qt.SolidLine))
    painter.drawText(int(self.x + 600 / 2), int(600 + 600 / 2)-50, f"{int(self.x + 600 / 2)}, {int(600 + 600 / 2)}")
    print(int(self.x + 600 / 2))
    print(int(600 + 600 / 2))
    painter.setPen(QPen(QColor(0, 0, 0), 5, Qt.SolidLine))

    # 如果两圆心之间距离<=300+150就画线
    # 移动的圆心坐标(self.x,900)
    # 所有圆的圆心坐标()
    for distance in range(10):
        if np.sqrt(np.square(int(self.x + 600 / 2) - x_Center_list[distance]) +
                   np.square(900 - y_Center_list[distance])) <= 450:
            painter.drawLine(int(self.x + 600 / 2), 900, x_Center_list[distance], y_Center_list[distance])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    x_Value_list = [1353, 1429, 767, 108, 183, 1443, 809, 512, 1041, 983]
    y_Value_list = [487, 915, 915, 299, 336, 525, 981, 925, 983, 910]
    main = DrawAll()
    main.show()
    sys.exit(app.exec_())