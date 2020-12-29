
class Config():
  DEBUG = False
  TESTING = False

  GARAGE_DOOR_CONFIG = {
    "Type": "Emulator"
  }

class ProductionConfig(Config):
  GARAGE_DOOR_CONFIG = {
    "I2C_Bus": 1,
    "I2C_Address": 0x10,
    "Register": 1,
    "Type": "Hardware"
  }

class DevelopmentConfig(Config):
  DEBUG = True

class TestingConfig(Config):
  TESTING = True
