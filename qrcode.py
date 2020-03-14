
from MyQR import myqr
from PyQt5.QtWidgets import QFileDialog


# 生成二维码的保存路径
def saveqrcodepath(self):
    qrcodepath = QFileDialog.getExistingDirectory(self, "choose directory",
                                                  "/Users/wulongxiang/PycharmProjects/wangyi")
    return qrcodepath


# 选择制作二维码的图片路径
def choosepicturepath(self):
    picturepath = QFileDialog.getOpenFileNames(self, "多文件选择", "/Users/wulongxiang/PycharmProjects/wangyi",
                                               "所有文件 (*);;图片文件 (*.png)")
    # 元组转换
    return picturepath[0][0]


# 制作二维码
def makeqrcode(words, picture, savepath, savename):
    # words = self.urllineEdit.text()
    # picture = self.pictureedit.text()
    # savepath = self.qrcodeedit.text()
    # savename = self.qrcodenameEdit.text()
    myqr.run(words, version=1, level='H', picture=picture,
             colorized=True, contrast=1.0, brightness=1.0,
             save_name=savename, save_dir=savepath)

