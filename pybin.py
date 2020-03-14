# -*- coding: utf-8 -*-
# 将图像音视频等资源文件隐藏在代码中
import os
import base64
from io import BytesIO


def bin2module(bin_file, py_file=None):
    """二进制文件转存为python模块

    bin_file    - 二进制文件名
    py_file     - 生成的模块文件名，默认使用二进制文件名，仅更改后缀名
    """

    fpath, fname = os.path.split(bin_file)
    fn, ext = os.path.splitext(fname)
    if not py_file:
        py_file = os.path.join(fpath, '%s.py' % fn)

    with open(bin_file, 'rb') as fp:
        content = fp.read()

    content = base64.b64encode(content)
    content = content.decode('utf8')

    with open(py_file, 'w') as fp:
        fp.write('# -*- coding: utf-8 -*-\n\n')
        fp.write('import base64\n')
        fp.write('from io import BytesIO\n\n')
        fp.write('content = """%s"""\n\n' % content)
        fp.write('def get_fp():\n')
        fp.write('    return BytesIO(base64.b64decode(content.encode("utf8")))\n\n')
        fp.write('def save(file_name):\n')
        fp.write('    with open(file_name, "wb") as fp:\n')
        fp.write('        fp.write(base64.b64decode(content.encode("utf8")))\n')


if __name__ == '__main__':
    # 将背景图片转存为icon.py
    bin2module('/Users/wulongxiang/PycharmProjects/wangyi/image/1.jpg', 'icon.py')
