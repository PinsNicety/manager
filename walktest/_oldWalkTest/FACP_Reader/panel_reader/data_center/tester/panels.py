from .device import *

class Panel:

    def __init__(self, data_file, test_file, panel_type):
        """Constructor for Panel Class."""
        self.panel_type = panel_type
        self.data_file = data_file
        self.test_file = test_file
        self.devices = {
            "detectors": {},
            "modules": {}
        }

    def __str__(self):
        """returns the panel_type of Object identification"""
        return self.panel_type

    def create_device(self, state, type_code, location, address):
        """Creates either detector or module based on parameters."""
        if address[3] == 'D':
            detector = Detector(state, type_code, location, address)
            self.devices["detectors"][detector.__str__()] = detector
        elif address[3] == 'M':
            module = Module(state, type_code, location, address)
            self.devices["modules"][module.__str__()] = module

class TwoThirtyThirty(Panel):

    def read_device_list(self):
        """
        Reads from data_file and adds each device to devices.
        Returns devices to the DataCenter object.
        """
        with open(self.data_file, 'r') as data_file:
            counter = 0
            for line in data_file:
                if counter == 0:
                    state = line[:7].strip()
                    type_code = line[7:20].strip()
                    location = line[20:54].strip()
                    counter += 1
                elif counter == 1:
                    counter  += 1
                elif counter == 2:
                    address = line[69:77].strip()
                    counter += 1
                elif counter == 3:
                    self.create_device(state, type_code, location, address)
                    counter = 0
            return self.devices

    def read_test_device_list(self):
        """
        Reads from test_file and adds each event to event_list.
        Returns the event_list to the DataCenter object.
        """
        with open(self.test_file, 'r') as test_file:
            last_line = ''
            self.event_list = []
            for line in test_file:
                snippit = line[:4]
                if snippit == 'SUPE' or snippit == 'FIRE':
                    last_line = snippit
                    continue
                if last_line == 'SUPE':
                    time = line[41:67].strip()
                    test_address = line[72:79].strip()
                    last_line = ''
                    self.event_list.append([test_address, time])
                elif last_line == 'FIRE':
                    test_address = line[72:79].strip()
                    time = line[41:67].strip()
                    last_line = ''
                    self.event_list.append([test_address, time])
            return self.event_list

class SixForty(Panel):

    def read_device_list(self):
        """
        Reads from data_file and adds each device to devices.
        Returns devices to the DataCenter object.
        """
        with open(self.data_file, 'r') as data_file:
            for line in data_file:
                state = line[:7].strip()
                type_code = line[7:20].strip()
                location = line[20:54].strip()
                address = "L0" + line[75:80].strip()
                self.create_device(state, type_code, location, address)
            return self.devices

    def read_test_device_list(self):
        """
        Reads from test_file and adds each event to event_list.
        Returns the event_list to the DataCenter object.
        """
        with open(self.test_file, 'r') as test_file:
            self.event_list = []
            for line in test_file:
                snippit = line[:5]
                if snippit == 'ALARM':
                    time = line[61:75].strip()
                    test_address = "L0" + line[75:80].strip()
                    self.event_list.append([test_address, time])
            return self.event_list

class ThreeTwenty(Panel):

    def read_device_list(self):
        """
        Reads from data_file and adds each device to devices.
        Returns devices to the DataCenter object.
        """
        with open(self.data_file, 'r') as data_file:
            for line in self.data_file:
                state = line[:7].strip()
                type_code = line[7:20].strip()
                location = line[20:54].strip()
                address = "L0" + line[75:80].strip()
                self.create_device(state, type_code, location, address)
            return self.devices

    def read_test_device_list(self):
        """
        Reads from test_file and adds each event to event_list.
        Returns the event_list to the DataCenter object.
        """
        with open(self.test_file, 'r') as test_file:
            self.event_list = []
            for line in test_file:
                snippit = line[:6]
                if snippit == 'ALARM:':
                    time = line[61:75].strip()
                    test_address = "L0" + line[75:80].strip()
                    self.event_list.append([test_address, time])
                elif snippit == 'ACTIVE':
                    time = line[61:75].strip()
                    test_address = "L0" + line[75:80].strip()
                    self.event_list.append([test_address, time])
            return self.event_list
