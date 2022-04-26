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

class KCube():
    
    def __init__(self):
        pass
    def init(self,sn):
        clr.AddReference("ThorLabs.MotionControl.KCube.DCServoCLI")
        from Thorlabs.MotionControl.KCube.DCServoCLI import KCubeDCServo
        print(DeviceManagerCLI.BuildDeviceList())
        device = KCubeDCServo.CreateKCubeDCServo(sn)
        device.Connect(sn)
        POLLING_INTERVAL = 250
        ENABLE_SLEEP_TIME = 0.1
        INIT_TIMEOUT = 5000
        device.WaitForSettingsInitialized(INIT_TIMEOUT)
        device.StartPolling(POLLING_INTERVAL)
        device.EnableDevice()
        config = device.LoadMotorConfiguration(sn)
        print(f'position {Decimal.ToDouble(device.DevicePosition)}')
        self.device = device
        
    def home(self):
        self.device.Home(0)
        
    def move_to(self, position):
        self.device.MoveTo(Decimal(position),0)
    
    def get_position(self):
        return Decimal.ToDouble(self.device.DevicePosition)
        
    def disconnect(self):
        self.device.Disconnect()
        
    def stop_immediate(self):
        self.device.StopImmediate()
        
    def move_continuous(self, orientation = 'cw'):
        if orientation == 'cw':
            self.device.MoveContinuous(1)
        elif orientation == 'ccw':
            self.device.MoveContinuous(2)


if __name__ is "__main__":
    # for testing and debuging
    device = LongTravelStage()
    device.init(serial = '45252134')
    print('device.home()')
    print('device.move_to(100)')
