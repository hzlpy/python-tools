# -*- coding: utf-8 -*-
#!usr/bin env python

import os
import logging
import datetime

def removeFileInFirstDir(targetDir):
    logging.basicConfig(level=logging.INFO, filename = 'E:/remove.log')
    for file in os.listdir(targetDir):
        targetFile = os.path.join(targetDir, file)
        if os.path.isfile(targetFile):
            os.remove(targetFile)
    logging.info('REMOVE file in %s %s' % (targetDir ,datetime.datetime.now()));


if __name__ == '__main__':
    targetDir = 'E:/log'
    removeFileInFirstDir(targetDir)
