from data_module import DataCenter

dc = DataCenter()
dc.read_device_list()
dc.print_devs()
dc.read_test_device_list()
dc.update_test_status()
dc.print_test_results()
