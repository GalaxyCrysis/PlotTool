from PyQt4 import QtGui,QtCore, uic
from DBimporter import DBimporter
from localfileUploader import fileUploader
import matplotLib
# global variable dataframe
dataframe = 0
dfList = {}

class mainWindow(QtGui.QMainWindow):

    def __init__(self):
        #init mainwindow
        super(mainWindow, self).__init__()
        uic.loadUi("main.ui", self)
        self.setWindowTitle("PlotTool")
        self.addMenu()


        self.plotButton.clicked.connect(self.plot)



        self.show()

        #add menu and its actions
    def addMenu(self):
        importMenu = self.menuBar().addMenu("Import Dataset")
        importMenu.addAction("Import from Database", self.importDatabase)
        importMenu.addAction("Import from local file", self.importFile)

        #get the data from ui and plot
    def plot(self):
        #get dataframe
        items = self.nameList.selectedItems()
        for i in list(items):
            data = str(i.text())
            df = dfList[data]
        #get geometry from list
        items = self.geometryList.selectedItems()
        for i in list(items):
            geom = str(i.text())
        #get style from style list
        items = self.styleList.selectedItems()
        for i in list(items):
            style = str(i.text())

        #get x and y axes data names
        xaxisData = self.xaxisEdit.text()
        yaxisData = self.yaxisEdit.text()
        #get x and y axes label
        xaxisLabel = self.xlabelEdit.text()
        yaxisLabel = self.ylabelEdit.text()

        #get date formatter
        if self.dformatterCheck.isChecked():
            dformatter = True
        else:
            dformatter = False
        dformatterText = self.dformatterEdit.text()

        #get data for subplot adjust
        if self.subplotCheck.isChecked():
            subplotCheck = True
        else:
            subplotCheck = False
        sublot_left = self.leftEdit.text()
        sublot_bottom = self.bottomEdit.text()
        subplot_right = self.rightEdit.text()
        subplot_top = self.topEdit.text()
        subplot_wspace = self.wspaceEdit.text()
        subplot_hspace = self.hspaceEdit.text()

        #get x and y lim
        xlim = self.xlimEdit.text()
        ylim = self.ylimEdit.text()

        #get line-plot attributes
        line_attributes = self.lineattrEdit.text()
        #multi line check
        if self.multilineCheck.isChecked():
            multiline = True
        else:
            multiline = False
        #get title
        title = self.titleEdit.text()

        #get scatter settings
        color_array = self.color_arrayEdit.text()
        marker = self.markerEdit.text()

        #get bar plot settings
        bar_width = self.boxwidthEdit.text()
        bar_color = self.boxcolorEdit.text()

        if self.boxdateCheck.isChecked():
            boxdate = True
        else:
            boxdate = False

        #get histogram settings
        hist_color = self.histcolorEdit.text()
        histtype = str(self.histBox.currentText())
        histalign = self.histalignEdit.text()
        histnumber = self.histnumberEdit.text()
        histlabel = self.histlabelEdit.text()

        #boxplot settings
        sym = self.symEdit.text()
        box_widths = self.boxwidthsEdit.text()
        if self.notchCheck.isChecked():
            notch = True
        else:
            notch = False


        #plot the data

        if geom == "line" or geom == "candlesticks" or geom =="bar" or geom=="pie":
            matplotLib.plot(df, geom, style, xaxisData, yaxisData, xaxisLabel, yaxisLabel, dformatter, dformatterText,
                            subplotCheck,
                            sublot_left, sublot_bottom, subplot_right, subplot_top, subplot_wspace, subplot_hspace,
                            xlim, ylim, line_attributes, title, multiline, bar_width, bar_color, boxdate)
        elif geom == "scatter":
            matplotLib.scatter(df,xaxisData,yaxisData,xaxisLabel,yaxisLabel,dformatter,dformatterText,xlim,ylim,subplotCheck,
                               sublot_left,sublot_bottom,subplot_right,subplot_top,subplot_wspace,subplot_hspace,title,marker,color_array)

        elif geom== "histogram":
            matplotLib.hist(df,yaxisData,xaxisData,histnumber,histtype,hist_color,title,histlabel,histalign,xaxisData, yaxisData,dformatter,
                            dformatterText,subplotCheck, sublot_left, sublot_bottom, subplot_right, subplot_top, subplot_wspace,
                            subplot_hspace)

        elif geom == "boxplot":
            matplotLib.boxplot(dataframe, xaxisData, sym, xaxisLabel, title,box_widths, notch, subplotCheck,
                               subplot_right, subplot_top, sublot_left, sublot_bottom, subplot_hspace, subplot_wspace)






    #import data from a local file
    def importFile(self):
        uploader = fileUploader()
        uploader.exec()

        #get data
        if uploader.close():
            global dataframe
            tablename, dataframe = uploader.importData()
            self.saveobjects(dataframe, tablename)





    #import data from database
    def importDatabase(self):
        importer = DBimporter()
        importer.exec()
        if importer.close():
            global dataframe
            tablename,dataframe = importer.importdata()
            self.saveobjects(dataframe, tablename)


    def saveobjects(self, df, tablename):
        shape = df.shape
        # put name of the dataframe, obs and variables in the widgetlist
        var = tablename + "  " + str(shape[0]) + " obj. of " + str(shape[1]) + " variables"
        # add to widgetlist
        item = QtGui.QListWidgetItem(var)
        self.dataList.addItem(item)
        # add to nameList
        name = QtGui.QListWidgetItem(tablename)
        self.nameList.addItem(name)

        # put data in global dataframe list

        dfList[tablename] = df


















