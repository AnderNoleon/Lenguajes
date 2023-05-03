from PyQt5.QtWidgets import QApplication
from views import MainView
import sys

app = QApplication(sys.argv)
window = MainView()
window.show()


sys.exit(app.exec_())