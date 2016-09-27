# !/usr/bin/env python
# -*- coding: utf-8 -*-
import os

def process_exist(process_name):
    process_lock = '/root/phxsql/tools/' + process_name + '.lock'
    # print(process_lock)
    os.system('ps -ef | grep %s | grep -v grep >%s' % (process_name, process_lock))
    if not(os.path.getsize(process_lock)):
	    print('%s is not exist. Will you want to restart it ?' % process_name)
    else:
	    print ('%s is running.' % process_name)

if __name__ == '__main__':
    process_exist('mysqld')
    process_exist('phxbinlogsvr')
    process_exist('phxsqlproxy')

