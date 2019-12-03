class QtLed(QWidget):

    def __init__(self, color=None):

        self.ledIcon = QLabel()
        self.ledIcon.setObjectName('ledIcon')

        self.changeColor(color)

        QWidget.__init__(self)
        layout = QVBoxLayout(self)
        layout.addWidget(self.ledIcon)

        self.ledIcon.setAlignment(Qt.AlignHCenter)
        self.ledIcon.setContentsMargins(0, 0, 0, 0)
        layout.setContentsMargins(0, 0, 0, 0)

    def changeColor(self, color):

        pixmap = QPixmap('img/offLED.png')
        if color == "green":
            pixmap = QPixmap('img/greenLED.png')
        if color == "red":
            pixmap = QPixmap('img/redLED.png')
        pixmap = pixmap.scaled(15, 15, Qt.KeepAspectRatio)

        self.ledIcon.setPixmap(pixmap)
