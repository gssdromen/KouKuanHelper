# coding:UTF-8

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui  import *
from PyQt4.QtCore  import *
import View
from HttpHelper import HttpHelper
from Constants import Constants
from bs4 import BeautifulSoup
import sched, time
import thread
from datetime import datetime


class Main(QtGui.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.initUI()

    def initUI(self):
        self.ui = View.Ui_MainWindow()
        self.ui.setupUi(self)
        # 初始化httpHelper
        self.http = HttpHelper()
        self.constants = Constants()
        self.getCookies()
        self.getStatus()
        self.startTimerTask()

    def startTimerTask(self):
        thread.start_new_thread(self.updateTime,())

    def updateTime(self):
        while True:
            now_ = datetime.now()
            print now_
            timeStr = '%d:%d:%d' % (now_.hour, now_.minute, now_.second)
            self.updateUI(timeStr)
            time.sleep(10)

    @QtCore.pyqtSlot()
    def updateUI(self, timeStr):
        self.ui.text_time.setPlainText(timeStr)

    def checkOneLine(self, line):
        if u'记账中' in line:
            return True
        if u'处理中' in line:
            return True
        if u'待' in line or u'可疑' in line:
            return True
        return False

    def getStatus(self):
        result = []
        url = self.constants.baseurl + '/vfs2/feededuct/deductFeeOSMessage.html'
        html = BeautifulSoup(self.http.sendRequest('get', url))
        results = html.find('table', id='results').find('tbody')
        tds = results.findAll('td')
        for td in tds:
            result.append(td.text.strip())
        return result

    def getCookies(self):
        fileHandle = open('acc.txt', 'r')
        line = fileHandle.readline()
        aList = line.split('|')
        dic={}
        dic["loginName"] = aList[0]
        dic["password"] = aList[1]
        html = BeautifulSoup(self.http.sendRequest('post', self.constants.baseurl+"/vfs2/login.html", dic))
        # req = urllib2.Request(baseUrl+"/vfs2/login.html", urllib.urlencode(dic))
        # req.add_header("Referer", baseUrl+"/vfs2/login.html")
        # resp = urllib2.urlopen(req)
        # html = BeautifulSoup(resp.read())
        print html.find('title').text.encode('UTF-8')

def main():
    app = QtGui.QApplication([])
    ex = Main()
    ex.show()
    app.exec_()

if __name__ == '__main__':
    main()
