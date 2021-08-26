import os

class Settings:
    VERSION = '0.1.0'
    APP_TITLE = 'Template Application'
    PROJECT_NAME = 'Template Application'
    APP_DESCRIPTION = 'TG - @AKuzyashin\nhttps://github.com/Kuzyashin'

    SERVER_HOST = 'localhost'

    DEBUG = True

    APPLICATIONS = [
        'users'
    ]

    PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    BASE_DIR = os.path.abspath(os.path.join(PROJECT_ROOT, os.pardir))
    LOGS_ROOT = os.path.join(BASE_DIR, "app/logs")
    EMAIL_TEMPLATES_DIR = os.path.join(BASE_DIR, "app/templates/emails/build/")

    # DB_URL = 'sqlite://./test.db'
    DB_URL='postgres://postgres:postgres@localhost:5432/fast_template_tortoise'
    DB_CONNECTIONS = {
            'default': {
                'engine': 'tortoise.backends.asyncpg',
                'db_url': DB_URL,
                'credentials': {
                    'host': '',
                    'port': '',
                    'user': '',
                    'password': '',
                    'database': '',
                }
            },
        }

    SECRET_KEY = '3488a63e1765035d386f05409663f55c83bfae3b3c61a932744b20ad14244dcf'  # openssl rand -hex 32
    JWT_ALGORITHM = 'HS25'
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # 7 day

    EMAILS_FROM_NAME = 'VessaliTI'
    EMAILS_FROM_EMAIL = 'igorvessali@gmail.com'
    SMTP_USER = 'igorvessali@gmail.com'
    SMTP_HOST = 'smtp.gmail.com'
    SMTP_PORT = 587
    SMTP_TLS = True
    SMTP_PASSWORD = 'IMvm30251003'
    EMAIL_RESET_TOKEN_EXPIRE_HOURS = 1
    EMAILS_ENABLED = SMTP_HOST and SMTP_PORT and EMAILS_FROM_EMAIL
    LOGIN_URL = SERVER_HOST + '/api/auth/login/access-token'



    APPLICATIONS_MODULE = 'app'

    CORS_ORIGINS = [
        "http://localhost",
        "http://localhost:8080",
        "http://localhost:5000",
        "http://localhost:3000",
    ]
    CORS_ALLOW_CREDENTIALS = True
    CORS_ALLOW_METHODS = ["*"]
    CORS_ALLOW_HEADERS = ["*"]


settings = Settings()
