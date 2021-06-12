import os
class Config:
  SECRET_KEY = 'AMMAINGI'

class ProdConfig(Config):
  pass

class DevConfig(Config):
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://layersony:1q2w3e4r5t6y@localhost/oneminipress'
  DEBUG = True

config_options = {'development':DevConfig, 'production':ProdConfig}
