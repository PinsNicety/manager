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

class ExcelWriter:

    def __init__(self):
        """Constructor for the ExcelWriter Class."""
        self.wb = load_workbook(self.excel_sheet)
        self.ws_detectors = self.wb["Detectors"]
        self.ws_modules = self.wb["Modules"]

    def print_devs(self):
        '''
        Prints devices to spreadsheet
        Rework this section to create an object to handle all IO's with Excel
        '''
        detectors_counter = 1
        modules_counter = 1

        for detector in self.devices["detectors"]:
            self.ws_detectors["A" + str(detectors_counter)] = self.devices["detectors"][detector].state
            self.ws_detectors["B" + str(detectors_counter)] = self.devices["detectors"][detector].type_code
            self.ws_detectors["C" + str(detectors_counter)] = self.devices["detectors"][detector].location
            self.ws_detectors["D" + str(detectors_counter)] = self.devices["detectors"][detector].address
            self.ws_detectors["E" + str(detectors_counter)] = self.devices["detectors"][detector].test_status_str()

            detectors_counter += 1

        for module in self.devices["modules"]:
            self.ws_modules["A" + str(modules_counter)] = self.devices["modules"][module].state
            self.ws_modules["B" + str(modules_counter)] = self.devices["modules"][module].type_code
            self.ws_modules["C" + str(modules_counter)] = self.devices["modules"][module].location
            self.ws_modules["D" + str(modules_counter)] = self.devices["modules"][module].address
            self.ws_modules["E" + str(modules_counter)] = self.devices["modules"][module].test_status_str()
            modules_counter += 1

        self.wb.save(self.excel_sheet)

    def print_test_results(self):
        """Updates speadsheet with newly tested devices."""
        detectors_counter = 1
        modules_counter = 1

        for detector in self.devices["detectors"]:
            self.ws_detectors["E" + str(detectors_counter)] = self.devices["detectors"][detector].test_status_str()
            self.ws_detectors["F" + str(detectors_counter)] = self.devices["detectors"][detector].test_time
            detectors_counter += 1

        for module in self.devices["modules"]:
            self.ws_modules["E" + str(modules_counter)] = self.devices["modules"][module].test_status_str()
            self.ws_modules["F" + str(modules_counter)] = self.devices["modules"][module].test_time
            modules_counter += 1

        self.wb.save(self.excel_sheet)


class DataCenter(TextReader, ExcelWriter):

    def __init__(self, panel_type, device_list, test_history):
        """Constructor for the DataCenter Class
        Take files used and create picker in the menu system.
        """
        self.excel_sheet = 'media/walktest/walktest.xlsx'
        self.data_file = device_list
        self.test_file = test_history

        self.panel_type = panel_type
        self.event_list = []
        TextReader.__init__(self)
        ExcelWriter.__init__(self)

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
