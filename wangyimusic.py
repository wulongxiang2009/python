from urllib.request import urlretrieve

from PyQt5.QtWidgets import QFileDialog
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


# 调用浏览器
def webtest():
    # 设置火狐为无界面浏览器
    options = Options()
    options.add_argument('--headless')
    # 调用火狐浏览器
    driver = webdriver.Firefox(options=options)
    return driver


# 连接歌曲路径及歌曲名
def music_savepath(pathedit, songname):
    savemusicname = pathedit + '/{}.mp3'.format(songname)
    return savemusicname


# 提示信息
def log(songlist, tip, song_name):
    songlist.addItem(tip.format(song_name))


# 歌曲下载
def song_load(songlist, pathedit, item):
    song_id = item['song_id']
    song_name = item['song_name']
    song_url = 'https://music.163.com/song/media/outer/url?id={}.mp3'.format(song_id)
    path = music_savepath(pathedit, song_name)
    log(songlist, '歌曲：{},正在下载...', song_name)
    urlretrieve(song_url, path)
    log(songlist, '下载完毕：{},请试听...', song_name)


# 选择歌曲
def get_music_name(songlist, pathedit, songedit):
    url = 'https://music.163.com/#/search/m/?s={}&type=1'.format(songedit)
    driver = webtest()
    driver.get(url=url)
    driver.switch_to.frame('g_iframe')

    # 获取歌曲id
    req = driver.find_element_by_id('m-search')
    a_id = req.find_element_by_xpath('.//div[@class="item f-cb h-flag  "]/div[2]//a').get_attribute('href')
    song_id = a_id.split('=')[-1]
    # 获取歌曲名
    song_name = req.find_element_by_xpath('.//div[@class="item f-cb h-flag  "]/div[2]//b').get_attribute('title')

    item = {'song_id': song_id, 'song_name': song_name}

    # 调用下载函数
    song_load(songlist, pathedit, item)
    # 退出火狐浏览器
    driver.close()


def musicsavepath(self):
    musicpath = QFileDialog.getExistingDirectory(self, "choose directory",
                                                "/Users/wulongxiang/PycharmProjects/wangyi")
    return musicpath
