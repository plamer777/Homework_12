from os import path

ALLOWED = {'jpg', 'jpeg', 'gif', 'png'}
POST_SOURCE = path.join('data', 'posts.json')
LOG_PATH = path.join('logs', 'app_logs.log')
UPLOADS = 'uploads/images/'
LOG_FORMAT = "[%(asctime)s] : [%(levelname)s] : [%(message)s]"
