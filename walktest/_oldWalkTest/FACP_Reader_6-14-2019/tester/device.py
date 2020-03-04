class Device:

    def __init__(self, state, type_code, location, address):
        """"Constructor for the Device Class"""
        self.state = state
        self.type_code = type_code
        self.location = location
        self.address = address
        self.test_time = ''

    def __str__(self):
        """returns the address for Object Identification"""
        return self.address

    def test_status_str(self):
        """returns test status as a string"""
        return str(self.test_status)

    def loop(self):
        """returns the loop number in L01 form"""
        return self.address[:3]

class Detector(Device):
    def __init__(self, state, type_code, location, address, test_status=False):
        """
        Constructor for the Detector class
        Parent Class: Device
        """
        self.test_status = test_status
        self.device_type = 'Detector'
        super().__init__(state, type_code, location, address)

    def detector_number(self):
        """returns the detector number in D001 form"""
        return self.address[3:7]

class Module(Device):
    def __init__(self, state, type_code, location, address, test_status=False):
        """
        Constructor for the Module class
        Parent Class: Device
        """
        self.test_status = test_status
        self.device_type = 'Module'
        super().__init__(state, type_code, location, address)

    def module_number(self):
        """returns the module number in M001 form"""
        return self.address[3:7]
