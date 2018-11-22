import sys
from PySide2.QtWidgets import QApplication, QLabel, QPushButton

app = QApplication(sys.argv)


def say_hello():
    print("Button clicked, Hello!")

#label = QLabel("<font color=red size=40>Hello World!</font>")


# Create a button, connect it and show it
button = QPushButton("Click Me")
button.clicked.connect(say_hello)
button.show()

# Run the main QT loop
app.exec_()
