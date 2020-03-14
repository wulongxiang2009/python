import you_get
import sys
from PyQt5.QtWidgets import QFileDialog

def videosavepath(self):
    videopath = QFileDialog.getExistingDirectory(self, "choose directory",
                                            "/Users/wulongxiang/PycharmProjects/wangyi")
    return videopath


def download(url, path):
    sys.argv = ['you-get', '--playlist', '-o', '--debug', path, url]
    you_get.main()

