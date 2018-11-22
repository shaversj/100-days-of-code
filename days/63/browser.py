import sys
from PySide2.QtCore import QUrl
from PySide2.QtWidgets import QApplication
from PySide2.QtWebEngineWidgets import QWebEngineView

app = QApplication(sys.argv)

view = QWebEngineView()
view.load(QUrl("https://theverge.com"))
view.show()

app.exec_()
