import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton, QMessageBox

class ChessParser:
    def __init__(self):
        self.valid_moves = ["e4", "Nf3", "exd5", "O-O", "e8=Q", "Qh5+", "1.e4 e5"]  # Agrega más movimientos válidos según la gramática

    def validate_move(self, move):
        if move in self.valid_moves:
            return True
        else:
            return False

class ChessApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.parser = ChessParser()

    def initUI(self):
        self.setWindowTitle('Chess Game Parser')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.label = QLabel('Ingrese la partida en Notación Algebraica Estándar (SAN):')
        layout.addWidget(self.label)

        self.text_edit = QTextEdit()
        layout.addWidget(self.text_edit)

        self.validate_button = QPushButton('Validar Partida')
        self.validate_button.clicked.connect(self.validate_game)
        layout.addWidget(self.validate_button)

        self.setLayout(layout)

    def validate_game(self):
        game_input = self.text_edit.toPlainText().strip().split()
        invalid_moves = []

        for move in game_input:
            if not self.parser.validate_move(move):
                invalid_moves.append(move)

        if invalid_moves:
            QMessageBox.warning(self, 'Movimientos Inválidos', f'Movimientos inválidos: {", ".join(invalid_moves)}')
        else:
            QMessageBox.information(self, 'Validación Exitosa', 'Todos los movimientos son válidos.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ChessApp()
    ex.show()
    sys.exit(app.exec_())
