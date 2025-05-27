from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from components import FloorPlanCanvas, ControlPanel

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("2D Wind Flow Simulator")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.canvas = FloorPlanCanvas()
        self.control_panel = ControlPanel()

        self.layout.addWidget(self.canvas)
        self.layout.addWidget(self.control_panel)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec_())