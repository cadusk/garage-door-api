from smbus2 import SMBus

class RelayControllerDummy():
  def click(self):
    print("Simulating clicking the relay")

class RelayController():
  def __init__(self, device_bus, device_addr, register, click_delay=1.5):
    self.__bus = SMBus(device_bus)
    self.__addr = device_addr
    self.__register = register
    self.__click_delay = click_delay

  def __set(self, value):
    self.__bus.write_byte_data(self.__addr, self.__register, value)

  def click(self):
    self.__set(0xff)
    time.sleep(self.__click_delay)
    self.__off(0x00)

