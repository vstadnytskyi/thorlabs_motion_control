"""
"""

import clr
clr.AddReference("System")

import sys
import time
import numpy as np
import matplotlib.pyplot as plt
import random  # only used for dummy data

from System import String
from System import Decimal
from System.Collections import *

# constants
sys.path.append(r"C:\Program Files\Thorlabs\Kinesis")
serial = '45252134'

clr.AddReference("Thorlabs.MotionControl.Controls")
import Thorlabs.MotionControl.Controls

clr.AddReference("Thorlabs.MotionControl.DeviceManagerCLI")
clr.AddReference("Thorlabs.MotionControl.GenericMotorCLI")
clr.AddReference("Thorlabs.MotionControl.IntegratedStepperMotorsCLI")
from Thorlabs.MotionControl.DeviceManagerCLI import *
from Thorlabs.MotionControl.GenericMotorCLI import *
from Thorlabs.MotionControl.IntegratedStepperMotorsCLI import *

POLLING_INTERVAL = 250
ENABLE_SLEEP_TIME = 0.1
INIT_TIMEOUT = 5000


class LongTravelStage():

    def __init__(self):
        pass

    def init(self, serial):
        self.device = self.initialize_device(serial)

    def initialize_device(self,serial):
        from Thorlabs.MotionControl import IntegratedStepperMotorsCLI
        clr.AddReference("Thorlabs.MotionControl.DeviceManagerCLI")
        from time import sleep
        # the request to build the device list is critical to operation of this code
        device_list_result = DeviceManagerCLI.BuildDeviceList()
        device = Thorlabs.MotionControl.IntegratedStepperMotorsCLI.LongTravelStage.CreateLongTravelStage(serial)
        device.Connect(serial)
        device.WaitForSettingsInitialized(INIT_TIMEOUT) #I think this is a crucial step in the initializatio
        device.EnableDevice()
        config = device.LoadMotorConfiguration(serial)
        deviceInfo = device.GetDeviceInfo()
        return device

    def print_positions(device):
        self.device.RequestPosition()

        return Decimal.ToDouble(self.device.DevicePosition)

    def home(self):
        """
        """
        self.device.Home(0)

    def is_homed(self):
        return device.device.Status.IsHomed

    def move_to(self,pos):
        """
        """
        self.device.MoveTo(Decimal(pos),0)

    def get_postiion(self):
        """
        returns current position
        """
        clr.AddReference("System")
        from System import Decimal
        return  Decimal.ToDouble(self.device.DevicePosition)

    def get_backlash(self):
        """
        returns current backlash settings
        """
        return Decimal.ToDouble(device.device.GetBacklash())

    def disconect(self):
        """
        """
        self.device.Disconnect()


if __name__ is "__main__":
    # for testing and debuging
    device = LongTravelStage()
    device.init(serial = '45252134')
    print('device.home()')
    print('device.move_to(100)')
