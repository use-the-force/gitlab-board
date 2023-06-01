timeout = 60
workers = 4
worker_connections = 15
name = 'config'
bind = '0.0.0.0:8000'
accesslog = '-'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s %(D)s "%(f)s" "%(a)s"'
