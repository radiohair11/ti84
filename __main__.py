from PyQt6.QtWidgets import QApplication, QGridLayout, QMainWindow, QPushButton, QWidget
from src.configs import WINDOW_SIZE_X, WINDOW_SIZE_Y, THETA, FIRST_ROW
from src.styles import SHIFT_BUTTON_STYLE, APPS_BUTTON_STYLE, ALPHA_BUTTON_STYLE, BLACK_BUTTON_STYLE, WHITE_BUTTON_STYLE


def get_button(name: str, style=BLACK_BUTTON_STYLE):
            btn = QPushButton(name)
            btn.setStyleSheet(style)
            return btn

class CalculatorWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("TI-84")
        self.setFixedSize(WINDOW_SIZE_X, WINDOW_SIZE_Y)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        button_layout = QGridLayout()

        button_layout.addWidget(get_button("Y="), 5, 0)
        button_layout.addWidget(get_button("WINDOW"), 5, 1)
        button_layout.addWidget(get_button("ZOOM"), 5, 2)
        button_layout.addWidget(get_button("TRACE"), 5, 3)
        button_layout.addWidget(get_button("GRAPH"), 5, 4)

        button_layout.addWidget(get_button("2ND", style=SHIFT_BUTTON_STYLE), 6, 0)
        button_layout.addWidget(get_button("MODE"), 6, 1)
        button_layout.addWidget(get_button("DEL"), 6, 2)
        button_layout.addWidget(get_button("\u2191", style=WHITE_BUTTON_STYLE), 6, 5)   # up arrow

        button_layout.addWidget(get_button("ALPHA", style=ALPHA_BUTTON_STYLE), 7, 0)
        button_layout.addWidget(get_button("X,T," + THETA + ",n"), 7, 1)
        button_layout.addWidget(get_button("STAT"), 7, 2)


        button_layout.addWidget(get_button("MATH"), 8, 0)
        button_layout.addWidget(get_button("APPS", style=APPS_BUTTON_STYLE), 8, 1)
        button_layout.addWidget(get_button("PRGM"), 8, 2)
        button_layout.addWidget(get_button("VARS"), 8, 3)
        button_layout.addWidget(get_button("CLEAR"), 8, 4)

        button_layout.addWidget(get_button("x\u207b\u00b9"), 9, 0)
        button_layout.addWidget(get_button("SIN"), 9, 1)
        button_layout.addWidget(get_button("COS"), 9, 2)
        button_layout.addWidget(get_button("TAN"), 9, 3)
        button_layout.addWidget(get_button("^"), 9, 4)

        button_layout.addWidget(get_button("x\u00b2"), 10, 0)
        button_layout.addWidget(get_button(","), 10, 1)
        button_layout.addWidget(get_button("("), 10, 2)
        button_layout.addWidget(get_button(")"), 10, 3)
        button_layout.addWidget(get_button("\u00f7", style=WHITE_BUTTON_STYLE), 10, 4)

        button_layout.addWidget(get_button("LOG"), 11, 0)
        button_layout.addWidget(get_button("7", style=WHITE_BUTTON_STYLE), 11, 1)
        button_layout.addWidget(get_button("8", style=WHITE_BUTTON_STYLE), 11, 2)
        button_layout.addWidget(get_button("9", style=WHITE_BUTTON_STYLE), 11 ,3)
        button_layout.addWidget(get_button("X", style=WHITE_BUTTON_STYLE), 11, 4)

        button_layout.addWidget(get_button("LN"), 12 ,0)
        button_layout.addWidget(get_button("4", style=WHITE_BUTTON_STYLE), 12, 1)
        button_layout.addWidget(get_button("5", style=WHITE_BUTTON_STYLE), 12, 2)
        button_layout.addWidget(get_button("6", style=WHITE_BUTTON_STYLE), 12, 3)
        button_layout.addWidget(get_button("-", style=WHITE_BUTTON_STYLE), 12, 4)

        button_layout.addWidget(get_button("STO>"), 13, 0)
        button_layout.addWidget(get_button("1", style=WHITE_BUTTON_STYLE), 13, 1)
        button_layout.addWidget(get_button("2", style=WHITE_BUTTON_STYLE), 13, 2)
        button_layout.addWidget(get_button("3", style=WHITE_BUTTON_STYLE), 13, 3)
        button_layout.addWidget(get_button("+", style=WHITE_BUTTON_STYLE), 13, 4)

        button_layout.addWidget(get_button("ON"), 14, 0)
        button_layout.addWidget(get_button("0"), 14, 1)
        button_layout.addWidget(get_button(".", style=WHITE_BUTTON_STYLE), 14, 2)
        button_layout.addWidget(get_button("(-)", style=WHITE_BUTTON_STYLE), 14, 3)
        button_layout.addWidget(get_button("ENTER", style=WHITE_BUTTON_STYLE), 14, 4)

        widget = QWidget()
        widget.setLayout(button_layout)
        self.setCentralWidget(widget)

        

if __name__ == '__main__':
    app = QApplication([])
    window = CalculatorWindow()
    window.show()
    app.exec()