#  下载歌曲相关的库
#  作者微信号：wulongxiang2009

# mac系统需要ssl权限
import ssl
import sys
import webbrowser

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPalette, QBrush
from PyQt5.QtWidgets import QApplication, QMainWindow

# 导入背景图片icon.py
import icon
# 导入二维码制作所需的函数
from qrcode import *
# 导入全网解析tab里的接口函数
from urljiekou import getjiekou
# 导入视频下载tab里的函数
from videodownload import download, videosavepath
# 导入qt5界面.py
from wangyi import *
# 导入网易音乐tab里用到的函数
from wangyimusic import *

ssl._create_default_https_context = ssl._create_unverified_context
# 利用icon.py里的save函数将icon.py的图片资源释放到当前目录
icon.save('2.jpg')

# 背景图片，利用释放的资源文件来换肤
backgroudpath = ['2.jpg']
playlist = ''
formatshipin = ''
i = 0
path = ''


# 使用PyQt5 Designer PyUic生成的Ui_MainWindow类,自定义类
class MyMainDialog(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyMainDialog, self).__init__()
        self.setupUi(self)

        # 如需使窗口透明，所在类初始化函数中设置如下属性
        # self.setAttribute(Qt.WA_TranslucentBackground, True)
        # 窗口无边框化，所在类初始化函数中设置如下属性
        self.setWindowFlags(Qt.FramelessWindowHint)

        # 网页tab 退出程序
        self.btnexit.clicked.connect(self.btnexitClick)
        self.btnexit_2.clicked.connect(self.btnexitClick)
        self.btnexitshipin.clicked.connect(self.btnexitClick)
        self.btnqrcodeexit.clicked.connect(self.btnexitClick)

        # 网易音乐
        self.btnstart.clicked.connect(self.btnstartmusicClick)
        self.btnsave.clicked.connect(self.btnsavemusicClick)

        # 视频下载
        self.btnstartshipin.clicked.connect(self.btnstartshipinClick)
        # 绑定视频保存目录
        self.btnsaveshipin.clicked.connect(self.btnsaveshipinClick)

        # 全网解析
        self.btnbofang.clicked.connect(self.open_browser)
        self.btnqingchu.clicked.connect(self.clear)

        # 二维码制作
        self.btnpicture.clicked.connect(self.choosepicture)
        self.btnqrcode.clicked.connect(self.saveqrcode)
        self.btnzhizuo.clicked.connect(self.qrcodezhizuo)

    # 生成二维码的保存路径
    def saveqrcode(self):
        self.qrcodeedit.setText(saveqrcodepath(self))

    # 选择制作二维码的图片路径
    def choosepicture(self):
        self.pictureedit.setText(choosepicturepath(self))

    # 制作二维码
    def qrcodezhizuo(self):
        words = self.urllineEdit.text()
        picture = self.pictureedit.text()
        savepath = self.qrcodeedit.text()
        savename = self.qrcodenameEdit.text()
        makeqrcode(words, picture, savepath, savename)

    def clear(self):
        self.editurl.setText('')

    def open_browser(self):
        locaction_content = getjiekou("http://www.qmaile.com/")
        if self.rbtn1.isChecked():
            parser_url1 = locaction_content[0]
            webbrowser.open(parser_url1 + self.editurl.text())
            print(parser_url1 + self.editurl.text())

        elif self.rbtn2.isChecked():
            parser_url2 = locaction_content[1]
            webbrowser.open(parser_url2 + self.editurl.text())
            print(parser_url2 + self.editurl.text())

        elif self.rbtn3.isChecked():
            parser_url3 = locaction_content[2]
            webbrowser.open(parser_url3 + self.editurl.text())
            print(parser_url3 + self.editurl.text())

        elif self.rbtn4.isChecked():
            parser_url4 = locaction_content[3]
            webbrowser.open(parser_url4 + self.editurl.text())
            print(parser_url4 + self.editurl.text())

        elif self.rbtn5.isChecked():
            parser_url5 = locaction_content[4]
            webbrowser.open(parser_url5 + self.editurl.text())
            print(parser_url5 + self.editurl.text())

    # 视频保存路径
    def btnsaveshipinClick(self):

        self.patheditshipin.setText(videosavepath(self))

    # 开始视频下载事件
    def btnstartshipinClick(self):
        url = self.shipinedit.text()
        download(url, path)

    # 开始下载歌曲函数
    def btnstartmusicClick(self):
        musiclist = self.songlist
        musicpath = self.pathedit.text()
        musicname = self.songedit.text()
        get_music_name(musiclist, musicpath, musicname)

    # 保存音乐路径函数
    def btnsavemusicClick(self):
        self.pathedit.setText(musicsavepath(self))

    def btnexitClick(self):
        self.close()

    # 定义鼠标点击事件
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            if event.button() == QtCore.Qt.LeftButton:
                self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
        event.accept()

    # 定义鼠标移动事件
    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

    # 窗体重绘事件
    def resizeEvent(self, event):
        palette = QPalette()
        pix = QPixmap(backgroudpath[i])
        pix = pix.scaled(self.width(), self.height())
        palette.setBrush(QPalette.Background, QBrush(pix))
        self.setPalette(palette)

    #  设置键盘退出快捷键
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    root = MyMainDialog()
    root.show()
    sys.exit(app.exec_())
