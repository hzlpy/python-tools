# !/usr/bin/env python
# -*- coding: utf-8 -*-
import os
mysql_process = '/root/phxsql/tools/mysqld.lock'
phxbinlogsvr_process = '/root/phxsql/tools/phxbinlogsvr.lock'
phxsqlproxy_process = '/root/phxsql/tools/phxsqlproxy.lock'
os.system('ps -ef | grep mysqld | grep -v grep >%s' % mysql_process)
os.system('ps -ef | grep phxbinlogsvr | grep -v grep >%s' % phxbinlogsvr_process)
os.system('ps -ef | grep phxsqlproxy | grep -v grep >%s' % phxsqlproxy_process)
if not(os.path.getsize(mysql_process)):
    print('mysqld is not exist. Will you want to restart it ?')
else:
    print('mysqld is running.')

if not(os.path.getsize(phxbinlogsvr_process)):
    print('phxbinlogsvr is not exist. Will you want to restart it ?')
else:
    print('phxbinlogsvr is running.')

if not(os.path.getsize(phxsqlproxy_process)):
    print('phxsqlproxy is not exist. Will you want ti restart it ?')
else:
    print('phxsqlproxy is running.')

