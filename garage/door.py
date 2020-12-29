from enum import IntEnum

class DoorStatus(IntEnum):
  CLOSED=0
  OPEN=1

class GarageDoor():
  def __init__(self, relay_controller):
    self.__relay_controller = relay_controller
    self.__door_status = DoorStatus.CLOSED

  @property
  def status(self):
    print("Checking status of dummy device")
    return self.__door_status

  def open(self):
    self.__door_status = DoorStatus.OPEN
    self.__relay_controller.click()

  def close(self):
    self.__door_status = DoorStatus.CLOSED
    self.__relay_controller.click()
