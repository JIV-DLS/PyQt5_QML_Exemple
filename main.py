import sys, model
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication,  QWidget, QVBoxLayout

from PyQt5.QtQuickWidgets import QQuickWidget

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        self.model = model.PersonModel()
        quickWidget = QQuickWidget()
        #affectaion des ressources python au contexte qml
        quickWidget.rootContext().setContextProperty('PersonModel', self.model)
        quickWidget.rootContext().setContextProperty('current_model_size_from_model', self.model.rowCount())
        #affectation du fichier qml
        quickWidget.setSource(QUrl('ui.qml'))
        quickWidget.setResizeMode(QQuickWidget.SizeRootObjectToView)
        layout.addWidget(quickWidget)

myApp = QApplication(sys.argv)
ui = MainWindow()
ui.show()
sys.exit(myApp.exec_())

