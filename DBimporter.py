from PyQt4 import QtGui,QtCore,uic
import dbhandler
#global variable dataframe
dataframe = 0
class DBimporter(QtGui.QDialog):
    def __init__(self):
        #init the database importer
        super(DBimporter, self).__init__()
        uic.loadUi("DBimporter.ui",self)
        self.codeLabel.hide()
        self.codeText.hide()
        self.individualRadio.toggled.connect(self.showCodeBlock)


        #creating the buttonsgroups for the checkboxes and radiobuttons
        radiogroup = QtGui.QButtonGroup(self)
        radiogroup.addButton(self.mysqlRadio)
        radiogroup.addButton(self.sqliteRadio)
        radiogroup.addButton(self.mongodbRadio)

        datagroup = QtGui.QButtonGroup(self)
        datagroup.addButton(self.allRadio)
        datagroup.addButton(self.individualRadio)
        self.databox.hide()
        self.getdataButton.clicked.connect(self.getdata)
        self.importButton.clicked.connect(self.importdata)
        self.show()

    def showCodeBlock(self):
        # shows the codeblock if the individual checkbox is checked
        if self.individualRadio.isChecked():
            self.codeLabel.show()
            self.codeText.show()
        else:
            self.codeLabel.hide()
            self.codeText.hide()
    def importdata(self):
        self.close()
        return (self.tableInput.text(),dataframe)

    #get data from database
    def getdata(self):
        #get database information from line edits
        user = self.userInput.text()
        password = self.passwordInput.text()
        host = self.hostInput.text()
        port = self.portInput.text()
        database = self.databaseInput.text()
        table = self.tableInput.text()

        #get data from MYSQL
        if self.mysqlRadio.isChecked():
            #get the dataframe von mysql function
            if self.allRadio.isChecked():
                global dataframe
                dataframe = dbhandler.getMYSQL(user,password,host,port,database,table,"all")

                self.databox.show()
                self.textBrowser.setText(str(dataframe))

            elif self.individualRadio.isChecked():
                sql = self.codeText.text()
                global dataframe
                dataframe = dbhandler.getMYSQL(user,password,host,port,database,table,sql)
                self.databox.show()
                self.textBrowser.setText(str(dataframe))
        #get data from mongo db database
        elif self.mongodbRadio.isChecked():
            if self.allRadio.isChecked():
                global dataframe
                dataframe = dbhandler.getMONGODB(user,password,host,int(port),database,table,"all")
                self.databox.show()
                self.textBrowser.setText(str(dataframe))
            elif self.individualRadio.isChecked():
                query = self.codeText.text()
                global dataframe
                dataframe = dbhandler.getMONGODB(user,password,host,int(port),database,table,query)
                self.databox.show()
                self.textBrowser.setText(str(dataframe))








