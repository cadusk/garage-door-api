from .door import GarageDoor
from .relay import RelayController, RelayControllerDummy

class GarageDoorBuilder():
  @classmethod
  def build(cls, config):
    if config["Type"] == "Emulator":
      return cls.__build_emulator()

    elif config["Type"] == "Hardware":
      return cls.__build_hardware(config)

    else:
      raise "Unknown type of GarageDoor"

  @classmethod
  def __build_emulator(cls):
    return GarageDoor(RelayControllerDummy())

  @classmethod
  def __build_hardware(cls, config):
    bus = config["I2C_Bus"]
    address = config["I2C_Address"]
    register = config["Register"]
    
    return GarageDoor(RelayController(bus, address, register))
