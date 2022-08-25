from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys
import os
import requests
import threading
import bdwiki
import bing
from ui_main import *
import list1
from ui_list import *

search_list = []

class List(Ui_Dialog, QDialog):
    def __init__(self):
        global search_list
        super().__init__()
        self.setupUi(self)
        
        # 添加项目
        self.listWidget.clear()
        for s in search_list:
            self.listWidget.addItem(s["title"])
        self.textBrowser.setText(search_list[0]["text"])
        
        self.listWidget.itemDoubleClicked.connect(self.edit)
        self.pushButton.clicked.connect(self.open)

        self.show()

    def edit(self, item):
        # print(dir(item))
        text = ""
        url = ""
        item_text = item.text()
        for i in search_list:
            if i["title"] == item_text:
                text = i["text"]
                url = i["url"]
        if text == None:
            text = "获取中，请稍候重试" # requests.get(url).text

        self.textBrowser.setText(text)
        self.lineEdit.setText(url)

        

    def open(self):
        url = self.lineEdit.text()
        if os.name == "nt":
            os.system("start " + url)
        else:
            os.system("xdg-open " + url)

def getText():
    global search_list
    len = -1
    print("Thread started.")
    for s in search_list:
        len += 1
        try:
            if s["text"] == None:
                search_list[len]["text"] = requests.get(s["url"]).text
        except:
            pass
    print("Done")


class uSearch(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.info.setText("<center>当前版本：V1.0</center>")
        self.pushButton.clicked.connect(self.search)
        self.show()
    def search(self):
        global search_list
        keyword = self.lineEdit.text()
        wiki = bdwiki.search(keyword)
        search_list = [{"title":"百度百科", "text": wiki, "url":""}]
        bing_list = bing.search(keyword)
        for b in bing_list:
            try:
                search_list += [
                    {
                        "title":b[0],
                        "url":b[1],
                        "text":None
                    }
                ]
            except:
                pass
        print(search_list)
        self.childWindow = List()
        self.thread1 = threading.Thread(None, getText)
        self.thread1.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = uSearch()
    sys.exit(app.exec_())
