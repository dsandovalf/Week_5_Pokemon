import os
class Config():
    REGISTERED_USERS  = {
    'kevinb@codingtemple.com' :{"name":"Kevin","password":"abc123"},
    'a;ext@codingtemple.com' :{"name":"Alex","password":"Colt45"},
    'joelc@codingtemple.com' :{"name":"Joel","password":"MorphinTime"}
    }
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS")