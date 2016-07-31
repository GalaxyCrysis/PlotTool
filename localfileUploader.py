from PyQt4 import QtGui,QtCore, uic
import PyQt4.QtGui
import pandas as pd

class fileUploader(QtGui.QDialog):
    dataframe = 0

    def __init__(self):
        super(fileUploader, self).__init__()
        uic.loadUi("fileImporter.ui", self)

        self.dataLabel.hide()
        self.dataBrowser.hide()

        self.uploadButton.clicked.connect(self.importFile)
        self.importButton.clicked.connect(self.importData)

    #import data to the main window
    def importData(self):
        #get name of the dataframe
        tablename = self.dfnameEdit.text()
        self.close()
        return (tablename, dataframe)





    def importFile(self):
        #get file name from f dialog
        file_name = QtGui.QFileDialog.getOpenFileName(self, "Open file", "/home")

        #open file
        file = open(file_name, "r")

        #get the data
        file_type = str(self.typeBox.currentText())

        global dataframe

        if file_type == "csv":
            dataframe = pd.io.parsers.read_csv(file)

        elif file_type == "excel":
            dataframe = pd.ExcelFile(file)

        #show data box
        self.dataLabel.show()
        self.dataBrowser.show()
        self.dataBrowser.setText(str(dataframe))










