from PyQt6.QtWidgets import QApplication, QVBoxLayout, QGridLayout, QMainWindow, QPushButton, QWidget
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from src.configs import WINDOW_SIZE_X, WINDOW_SIZE_Y, THETA, FIRST_ROW
from src.styles import APP_STYLE, SHIFT_BUTTON_STYLE, APPS_BUTTON_STYLE, ALPHA_BUTTON_STYLE, BLACK_BUTTON_STYLE, WHITE_BUTTON_STYLE


def get_button(name: str, style=BLACK_BUTTON_STYLE):
            btn = QPushButton(name)
            btn.setStyleSheet(style)
            return btn
class Screen(FigureCanvas):

    def __init__(self, parent=None, width=4, height=4, dpi=96):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        self.axes.axis('off')
        super().__init__(fig)
class CalculatorWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        screen = Screen(self, width=1, height=1, dpi=100)

        self.setWindowTitle("TI-84")
        self.setFixedSize(WINDOW_SIZE_X, WINDOW_SIZE_Y)
        main_layout = QGridLayout()
        main_layout.addWidget(screen, 0, 0, 1, 1)
        button_layout = self._createButtons()
        main_layout.addLayout(button_layout, 1, 0, 2, 1)

        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

    def _createButtons(self):
        layout = QGridLayout()

        layout.addWidget(get_button("Y="), 0, 0)
        layout.addWidget(get_button("WINDOW"), 0, 1)
        layout.addWidget(get_button("ZOOM"), 0, 2)
        layout.addWidget(get_button("TRACE"), 0, 3)
        layout.addWidget(get_button("GRAPH"), 0, 4)

        layout.addWidget(get_button("\u2191", style=WHITE_BUTTON_STYLE), 1, 3, 1, 2)   # up arrow

        layout.addWidget(get_button("2ND", style=SHIFT_BUTTON_STYLE), 2, 0)
        layout.addWidget(get_button("MODE"), 2, 1)
        layout.addWidget(get_button("DEL"), 2, 2)
        layout.addWidget(get_button("\u2190", style=WHITE_BUTTON_STYLE), 2, 3)  # left arrow
        layout.addWidget(get_button("\u2192", style=WHITE_BUTTON_STYLE), 2, 4)  # right arrow

        layout.addWidget(get_button("ALPHA", style=ALPHA_BUTTON_STYLE), 3, 0)
        layout.addWidget(get_button("X,T," + THETA + ",n"), 3, 1)
        layout.addWidget(get_button("STAT"), 3, 2)
        layout.addWidget(get_button("\u2193", style=WHITE_BUTTON_STYLE), 3, 3, 1, 2)  # down arrow


        layout.addWidget(get_button("MATH"), 4, 0)
        layout.addWidget(get_button("APPS", style=APPS_BUTTON_STYLE), 4, 1)
        layout.addWidget(get_button("PRGM"), 4, 2)
        layout.addWidget(get_button("VARS"), 4, 3)
        layout.addWidget(get_button("CLEAR"), 4, 4)

        layout.addWidget(get_button("x\u207b\u00b9"), 5, 0)
        layout.addWidget(get_button("SIN"), 5, 1)
        layout.addWidget(get_button("COS"), 5, 2)
        layout.addWidget(get_button("TAN"), 5, 3)
        layout.addWidget(get_button("^"), 5, 4)

        layout.addWidget(get_button("x\u00b2"), 6, 0)
        layout.addWidget(get_button(","), 6, 1)
        layout.addWidget(get_button("("), 6, 2)
        layout.addWidget(get_button(")"), 6, 3)
        layout.addWidget(get_button("\u00f7", style=WHITE_BUTTON_STYLE), 6, 4)

        layout.addWidget(get_button("LOG"), 7, 0)
        layout.addWidget(get_button("7", style=WHITE_BUTTON_STYLE), 7, 1)
        layout.addWidget(get_button("8", style=WHITE_BUTTON_STYLE), 7, 2)
        layout.addWidget(get_button("9", style=WHITE_BUTTON_STYLE), 7 ,3)
        layout.addWidget(get_button("\u00d7", style=WHITE_BUTTON_STYLE), 7, 4) # multiply

        layout.addWidget(get_button("LN"), 8 ,0)
        layout.addWidget(get_button("4", style=WHITE_BUTTON_STYLE), 8, 1)
        layout.addWidget(get_button("5", style=WHITE_BUTTON_STYLE), 8, 2)
        layout.addWidget(get_button("6", style=WHITE_BUTTON_STYLE), 8, 3)
        layout.addWidget(get_button("-", style=WHITE_BUTTON_STYLE), 8, 4)

        layout.addWidget(get_button("STO\u2b9e"), 9, 0)
        layout.addWidget(get_button("1", style=WHITE_BUTTON_STYLE), 9, 1)
        layout.addWidget(get_button("2", style=WHITE_BUTTON_STYLE), 9, 2)
        layout.addWidget(get_button("3", style=WHITE_BUTTON_STYLE), 9, 3)
        layout.addWidget(get_button("+", style=WHITE_BUTTON_STYLE), 9, 4)

        layout.addWidget(get_button("ON"), 10, 0)
        layout.addWidget(get_button("0"), 10, 1)
        layout.addWidget(get_button(".", style=WHITE_BUTTON_STYLE), 10, 2)
        layout.addWidget(get_button("( - )", style=WHITE_BUTTON_STYLE), 10, 3)
        layout.addWidget(get_button("ENTER", style=WHITE_BUTTON_STYLE), 10, 4)

        return layout

if __name__ == '__main__':
    app = QApplication([])
    app.setStyleSheet(APP_STYLE)
    window = CalculatorWindow()
    window.show()
    app.exec()