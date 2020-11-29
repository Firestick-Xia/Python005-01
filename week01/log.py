"""
编写一个函数, 当函数被调用时，将调用的时间记录在日志中,
日志文件的保存位置建议为：/var/log/python- 当前日期 /xxxx.log
"""

import logging
import time
import os
import shutil


def record():
    path = os.getcwd()
    date = time.strftime('%Y-%m-%d', time.localtime())
    dir = path+'/var/log/' + 'python-' + date+ '/'

    if os.path.exists(dir):
        shutil.rmtree(dir)
    os.makedirs(dir)



    logging.basicConfig(filename=dir + '/test.log',
                        level=logging.INFO,
                        datefmt='%Y-%m-%d %H:%M,%S',
                        format='%(asctime)s %(name)-8s %(levelname)-8s [line:%(lineno)d] %(message)s')
    logging.info('it is called!')

if __name__ == '__main__':
    record()