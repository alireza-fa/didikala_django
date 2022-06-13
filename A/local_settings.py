SECRET_KEY = 'django-insecure-c2a^ar^*wsmx7l4u)5k9git_-d_n(tn62vt-4=ub!!@&ll(!z6'

DEBUG = True


# DB
DB_NAME = 'didikala'
DB_USER = 'didikala'
DB_PASS = 'didikala'
DB_HOST = 'localhost'
DB_PORT = 5432


# s3 amazon
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
AWS_STORAGE_BUCKET_NAME = ''
ASW_SERVICE_NAME = 's3'
AWS_s3_ENDPOINT_URL = ''
AWS_s3_FILE_OVERWRITE = False
