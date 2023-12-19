import os

class Config(object):
    APP_ID = int(os.environ.get("APP_ID", 28501381))
    API_HASH = os.environ.get("API_HASH", "1ec36e0c2bee22312d163f46299052c2")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6968270929:AAE8S0feUjlpA5LEt2fWJhrtS3moATORqXg")
    VIRUSTOTAL_API = os.environ.get("VIRUSTOTAL_API", "15a924da16e03c34778116fdbed6c3040adf8cd04e4b12c42eb851c63366386b")
    userid = int(os.environ.get('userid',1569238601))
