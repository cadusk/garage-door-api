from flask import Flask

app = Flask(__name__)

configurations = {
  'development': 'config.DevelopmentConfig',
  'production':  'config.ProductionConfig',
  'testing':     'config.TestingConfig'
}

app.config.from_object(
  configurations.get(app.config['ENV'].lower(), 'production'))
