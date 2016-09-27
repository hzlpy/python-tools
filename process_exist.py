# !/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import logging
import datetime

def process_exist(process_name):
    process_lock = '/root/phxsql/tools/' + process_name + '.lock'
    # print(process_lock)
    os.system('ps -ef | grep %s | grep -v grep >%s' % (process_name, process_lock))
    if not(os.path.getsize(process_lock)):
	    # print('%s is not exist. Will you want to restart it ?' % process_name)
        logging.info('%s is not exist. Will you want to restart it ?    %s' % (process_name, datetime.datetime.now()))
    else:
	    # print ('%s is running.' % process_name)
        logging.info('%s is running.    %s' % (process_name, datetime.datetime.now()))

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filename='/tmp/data/process_exist.log')
    logging.info('check whether process exist..    %s', datetime.datetime.now())
    process_exist('mysqld')
    process_exist('phxbinlogsvr')
    process_exist('phxsqlproxy')

