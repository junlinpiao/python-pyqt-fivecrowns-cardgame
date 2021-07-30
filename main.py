import sys
from PyQt5.QtWidgets import QApplication
from model.model import Model
from controller.main_controller import MainController

# Entry point of this software.
# Application class
class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.model = Model()
        self.main_controller = MainController(self.model)

if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())