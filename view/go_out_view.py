from PyQt5 import QtCore, QtWidgets
from view.go_out_view_ui import Ui_GoOut
from view.hand_view import HandWidget

class GoOutWidget(QtWidgets.QWidget):
    
    signal_continue = QtCore.pyqtSignal()

    def __init__(self, model):
        QtWidgets.QWidget.__init__(self)
        self._ui = Ui_GoOut()
        self._ui.setupUi(self)
        self._model = model

        self._ui.btn_ok.clicked.connect(self.onContinue)
        self.setup_gui()

    def setup_gui(self):
        first_gone_out_player = self._model.get_data('first_gone_out')
        first_gone_out_player_name = first_gone_out_player.get_player_name()
        self.setWindowTitle('Someone go out')
        self._ui.lbl_heading.setText("<span style='color: red'>\"{}\"</span> goes out!<br>Other players have only 1 chance.".format(first_gone_out_player_name))

        # show runs and books
        self.drop_hand_wgts = []
        scroll_wgt = self._ui.scrollAreaWidgetContents
        self.scroll_vLayout = QtWidgets.QVBoxLayout(scroll_wgt)
        self.lbl_info = QtWidgets.QLabel(scroll_wgt)
        self.lbl_info.setStyleSheet("font-size: 15px")
        self.lbl_info.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_info.setText("<span style='color: red'>\"{}\"</span>'s Runs and Blocks".format(first_gone_out_player_name))
        self.scroll_vLayout.addWidget(self.lbl_info)
        cur_drop_hands = first_gone_out_player.get_drop_hands()
        for drop_hand in cur_drop_hands:
            drop_hand_wgt = HandWidget(drop_hand, scroll_wgt.width() - 20, 160, scroll_wgt, True)
            drop_hand_wgt.show()
            self.scroll_vLayout.addWidget(drop_hand_wgt)
            self.drop_hand_wgts.append(drop_hand_wgt)
        self.spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.scroll_vLayout.addItem(self.spacerItem4)

    def onContinue(self):
        self.signal_continue.emit()
