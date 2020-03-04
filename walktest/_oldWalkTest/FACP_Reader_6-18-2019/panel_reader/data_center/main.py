import os


BASE_PATH = 'D:\\projects\\FACP_Reader\\panel_reader\\data_center\\'
file = os.path.join(BASE_PATH, 'static\\Springfield Bulk Mail_2-3030_Device List.txt')

with open(file, 'r') as file:
    for line in file:
        print(line)