#!usr/bin env python
import os
import datetime
import logging
import pyinotify


class MyEventHandler(pyinotify.ProcessEvent):
    logging.basicConfig(level=logging.INFO, filename='/tmp/data/monitor.log')
    logging.info('Starting monitor..')

    def process_IN_ACCESS(self, event):
	    # print('ACCESS event:', event.pathname)
	    logging.info('ACCESS event : %s %s' % (os.path.join(event.path, event.name), datetime.datetime.now()))

    def process_IN_ATTRIB(self, event):
	    # print('ATTRIB event:', event.pathname)
	    logging.info('ATTRIB event : %s %s' % (os.path.join(event.path, event.name), datetime.datetime.now()))
	
    def process_IN_CLOSE_NOWRITE(self, event):
	    # print('CLOSE_NOWRITE event:', event.pathname)
	    logging.info('CLOSE_NOWRITE event : %s %s' % (os.path.join(event.path, event.name), datetime.datetime.now()))
	
    def process_IN_CLOSE_WRITE(self, event):
	    # print('CLOSE_WRITE event:', event.pathname)
	    logging.info('CLOSE_WRITE event : %s %s' % (os.path.join(event.path, event.name), datetime.datetime.now()))
	
    def process_IN_CREATE(self, event):
	    # print('CREATE event:', event.pathname)
	    logging.info('CREATE event : %s %s' % (os.path.join(event.path, event.name), datetime.datetime.now()))
	
    def process_IN_DELETE(self, event):
	    # print('DELETE event:', event.pathname)
	    logging.info('DELETE event : %s %s' % (os.path.join(event.path, event.name), datetime.datetime.now()))
	
    def process_IN_MODIFY(self, event):
	    print('MODIFY event:', event.pathname)
		# if phxsqlproxy.conf is modified, restart phxsqlproxy
	    str1 = '/root/phxsql/etc/phxsqlproxy.conf'
	    if cmp(str1, event.pathname) == 0:
		    logging.info('phxsqlproxy.conf has been modified.')
		    # restart phxsqlproxy for reload .conf
		    os.system('python restart.py -pphxsqlproxy')
       
        # if phxbinlogsvr.conf is modified, restart phxbinlogsvr
	    str2 = '/root/phxsql/etc/phxbinlogsvr.conf'
		if cmp(str2, event.pathname) == 0:
		    logging.info('phxbinlogsvr.conf has been modified.')
			# restart phxbinlogsvr for reload .conf
	        os.system('python restart.py -pphxbinlogsvr')
        
        # if my.conf is modified, restart mysqld
        str3 = '/root/phxsql/etc/my.conf'
        if cmp(str3, event.pathname) == 0:
	        logging.info('my.conf has been modified.')
		    # restart mysql for reload .conf
	        os.system('python restart.py -pmysql')
	    logging.info('MODIFY event : %s %s' % (os.path.join(event.path, event.name), datetime.datetime.now()))
	
    def process_IN_OPEN(self, event):
	    # print('OPEN event:', event.pathname)
	    logging.info('OPEN event : %s %s' % (os.path.join(event.path, event.name), datetime.datetime.now()))
	
def main():
    # watch manager
    wm = pyinotify.WatchManager()
    mask = pyinotify.IN_CREATE | pyinotify.IN_DELETE | pyinotify.IN_MODIFY
	# wm.add_watch('/root/phxsql/etc', pyinotify.ALL_EVENTS, rec=True)
    wm.add_watch('/root/phxsql/etc', mask, rec=True)
    handler = MyEventHandler()

    notifier = pyinotify.Notifier(wm, handler, )
    notifier.loop()

if __name__ == '__main__':
    main()
