import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from matplotlib.finance import candlestick_ohlc
import matplotlib.style as stl
import numpy as np
def plot(dataframe, geom, style, xaxisData, yaxisData, xlabel, ylabel, dformatter, dformatterText, subplotCheck, left, bottom, right, top, wspace, hspace,xlim,ylim, lineattr,title, multiline, barwidth, barcolor, boxdate):
    stl.use(style)
    plt.figure()
    ax1 = plt.subplot2grid((1, 1), (0, 0))
    setLabels(xlabel, ylabel)
    ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
    #line plot
    if geom == "line":

        if multiline == True:

            #get the list from y data
            list = yaxisData.split(",")
            for line in list:
                plt.plot(dataframe[xaxisData], dataframe[line])

        else:

            plt.plot(dataframe[xaxisData], dataframe[yaxisData], lineattr)




    #plot candlesticks
    elif geom == "candlesticks":

        ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
        setLabels(xlabel, ylabel)

        ohlc = []
        #add values to ohlc and plot the candlesticks
        for x in range(0, len(dataframe["date"])):
            date = float(dataframe["date"][x])
            append_line = date, dataframe["openp"][x], dataframe["highp"][x], dataframe["lowp"][x], \
                          dataframe["closep"][x], dataframe["volume"][x]
            ohlc.append(append_line)
        candlestick_ohlc(ax1, ohlc, width=0.4, colorup="g", colordown="r")

        #bar plot
    elif geom == "bar":
        list = yaxisData.split(",")
        length = len(dataframe[xaxisData])
        color_list = barcolor.split(",")
        counter = 0
        rectList = []


        if boxdate == True:
            #convert date time
            datelist = []
            for x in range(0, len(dataframe[xaxisData])):
                date = dataframe[xaxisData][x]
                date = float(date)
                datelist.append(date)

            for item in list:
                rect = ax1.bar(datelist, dataframe[item],width=float(barwidth), color=color_list[counter], align="center")
                counter +=1
                rectList.append(rect)


        else:
            for item in list:
                rect = ax1.bar(dataframe[xaxisData], dataframe[item], width=float(barwidth), color=color_list[counter], align="center")
                counter +=1
                rectList.append(rect)
    #pie plot
    elif geom == "pie":
        ax1.pie(dataframe[xaxisData], labels=dataframe[yaxisData], autopct="%1.1f%%", counterclock=False, shadow=True)
        plt.title(title)





    #date formatter
    if dformatter == True:
        ax1.get_xaxis().set_major_formatter(mdates.DateFormatter(dformatterText))
    #subplot adjust
    if subplotCheck == True:
        plt.subplots_adjust(left=float(left), bottom=float(bottom), top=float(top), right=float(right),
                            wspace=float(wspace),
                            hspace=float(hspace))

    #limiter
    if xlim:
        xlim = setLims(xlim)
        ax1.set_xlim(xlim)
    if ylim:
        ylim = setLims(ylim)
        ax1.set_ylim(ylim)
    #set title
    setTitle(title)

    plt.show()

#plot scatter graph
def scatter(dataframe, xaxisData, yaxisData, xlabel, ylabel, dformatter, dformatterText, xlim, ylim, subplot_check,left, bottom, right, top, wspace, hspace, title, marker, color_array):
    #get length
    list= yaxisData.split(",")
    length = len(dataframe[list[0]])
    #set Title
    setTitle(title)
    #setLabel
    setLabels(xlabel,ylabel)

    ax1 = plt.subplot2grid((1, 1), (0, 0))
    #get color array
    list = color_array.split(",")
    color_array = []
    #create the color array for scatter plotting
    for color in list:
        array = [color] * length
        color_array = color_array + array

    #create data axes
    #x data create array
    x = np.array([]).reshape(0, length)


    list = xaxisData.split(",")
    for item in list:
        array = dataframe[item]
        x = np.vstack([x, array])
    #y data
    y = np.array([]).reshape(0, length)

    list = yaxisData.split(",")
    for item in list:
        array = dataframe[item]
        y = np.vstack([y, array])


    #plot scatter
    plt.scatter(x,y , marker=marker, c= color_array)



    # date formatter
    if dformatter == True:
        ax1.get_xaxis().set_major_formatter(mdates.DateFormatter(dformatterText))
    # subplot adjust
    if subplot_check == True:
        plt.subplots_adjust(left=float(left), bottom=float(bottom), top=float(top), right=float(right),
                            wspace=float(wspace),
                            hspace=float(hspace))

    # limiter
    if xlim:
        xlim = setLims(xlim)
        ax1.set_xlim(xlim)
    if ylim:
        ylim = setLims(ylim)
        ax1.set_ylim(ylim)

    plt.show()

#histogram plot
def hist(dataframe, data, range, numberOfBoxes, histtype, color, title, label, align, xlabel, ylabel, dformatter, dformattertext, subplot_check,left, bottom, right, top, wspace, hspace):
    fig = plt.figure()
    ax1 = plt.subplot2grid((1,1),(0,0))

    #get lists for multiple histograms
    list = data.split(",")
    color_list = color.split(",")
    label_list = label.split(",")
    counter = 0

    #get range of the

    #plot the data
    for item in list:
        ax1.hist(dataframe[item], int(numberOfBoxes), histtype=histtype,
                 align=align, label=label_list[counter], color=color_list[counter])
        counter +=1

        # date formatter
    if dformatter == True:
        ax1.get_xaxis().set_major_formatter(mdates.DateFormatter(dformattertext))
        # subplot adjust
    if subplot_check == True:
        plt.subplots_adjust(left=float(left), bottom=float(bottom), top=float(top), right=float(right),
                            wspace=float(wspace),
                            hspace=float(hspace))

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()

    plt.show()

def boxplot(dataframe,data, sym, ylabel, title, widths, notch, subplot_check, right, top, left, bottom, hspace, wspace):
    fig = plt.figure()
    ax1 = plt.subplot2grid((1,1),(0,0))

    plt.ylabel(ylabel)
    plt.title(title)


    ax1.boxplot(dataframe[data], sym=sym, widths=float(widths), notch=notch)


    plt.show()


     #subplot adjust
    if subplot_check == True:
        plt.subplots_adjust(left=float(left), bottom=float(bottom), top=float(top), right=float(right),
                            wspace=float(wspace),
                            hspace=float(hspace))






#get the lim and convert it to an array. finally return it
def setLims(stringlim):
    list = stringlim.split(",")
    lim = []
    for x in list:
        lim.append(float(x))
    return lim
def setTitle(title):
    if title:
        plt.title(title)
    else:
        plt.title("Graph")




def setLabels(xlabel, ylabel):
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)









