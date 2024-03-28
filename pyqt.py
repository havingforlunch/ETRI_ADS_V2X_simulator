import sys
from PyQt5.QtWidgets import *

import pyautogui, struct
from graph_chart import *

"""
app = QApplication(sys.argv)

root = MyWindow()
root.show()

test2 = MyWindow()
test2.show()
test2.close()
sys.exit(app.exec_())

"""

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setAcceptDrops(True)
        size_x , size_y = 800, 800
        width, height = pyautogui.size()
        self.setGeometry(width/80+width/1.5, height/8, (width*0.48)/1.5,(height)/1.5)


    def initUI(self):
        ads_chart = ads_speed_chart()
        car1_chart = car1_speed_chart()
        car2_chart = car2_speed_chart()
        data_wd = log_wiget()

        impMenu = QMenu('업데이트 속도 변경', self)
        impAct1 = QAction('느리게', self)
        impAct2 = QAction('보통', self)
        impAct3= QAction('빠르게', self)
        impMenu.addAction(impAct1)
        impMenu.addAction(impAct2)
        impMenu.addAction(impAct3)
        exitAction = QAction('&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        ########################################################

        menu = self.menuBar()
        menu_file = menu.addMenu("File")
        menu_edit = menu.addMenu("Edit")
        menu_sample = menu.addMenu("Sample")

        menu_file.addMenu(impMenu)
        menu_file.addAction(exitAction)

        self.chartlayout = QVBoxLayout()
        self.chartlayout.addWidget(ads_chart,100)
        self.chartlayout.addWidget(car1_chart, 100)
        self.chartlayout.addWidget(car2_chart, 100)

        self.up_frame = QFrame()
        self.up_frame.setLayout(self.chartlayout)

        layout = QVBoxLayout()
        layout.addWidget(self.up_frame, 70)
        layout.addWidget(data_wd, 50)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.setWindowTitle('Etri_0.8')

        # ADS 속도 그래프
        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(ads_chart.ads_plot_data)
        self.timer.start()
        # CAR1 속도 그래프
        self.timer2 = QtCore.QTimer()
        self.timer2.setInterval(50)
        self.timer2.timeout.connect(car1_chart.car1_plot_data)
        self.timer2.start()
        # CAR2,E_car 속도 그래프
        self.timer3 = QtCore.QTimer()
        self.timer3.setInterval(50)
        self.timer3.timeout.connect(car2_chart.car2_e_plot_data)
        self.timer3.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())