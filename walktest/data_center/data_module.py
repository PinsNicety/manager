import os
from .panels.panels import TwoThirtyThirty, SixForty, ThreeTwenty
from openpyxl import load_workbook, Workbook

class TextReader:

    def __init__(self):
        """Constructor for the TextReader Class."""
        self.panels = {
            "3030": TwoThirtyThirty,
            "640": SixForty,
            "320": ThreeTwenty
        }
        self.panel = self.panels[self.panel_type](self.data_file, self.test_file, self.panel_type)

    def read_device_list(self):
        """
        Creates Panel Object and runs the read_device_list() on this Panel.
        The panel will return a dictionary of devices that will be used by the DataCenter.
        devices = {"detectors": {} "modules": {}}
        """
        self.devices = self.panel.read_device_list()

    def read_test_device_list(self):
        """
        Runs read_test_device_list() on self.panel.
        self.panel will return a list of events.
        Event Format: [test_address, time]
        """
        self.event_list = self.panel.read_test_device_list()


class DataCenter(TextReader):

    def __init__(self, panel_type, device_list, test_history):
        """Constructor for the DataCenter Class
        Take files used and create picker in the menu system.
        """
        self.data_file = device_list
        self.test_file = test_history

        self.panel_type = panel_type
        self.event_list = []
        TextReader.__init__(self)

    def update_test_status(self):
        """
        Goes through event list and updates Device objects test_status to True,
        and updates test_time to the new test_time.
        """
        for event in self.event_list:
            if event[0] in self.devices["detectors"]:
                self.devices["detectors"][event[0]].test_status = True
                self.devices["detectors"][event[0]].test_time = event[1]
            elif event[0] in self.devices["modules"]:
                self.devices["modules"][event[0]].test_status = True
                self.devices["modules"][event[0]].test_time = event[1]
