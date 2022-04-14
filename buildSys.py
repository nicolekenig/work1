import os
import sys
from sys import argv

PATH_DATA_SYS = 'data_for_exercises/circuits/Data_Systems'
PATH_DATA_OBS = 'data_for_exercises/circuits/Data_Observations'


def readFiles():
    files = os.listdir(PATH_DATA_SYS)
    for file_name in files:
        if file_name.startswith('74') or file_name.startswith('c17'):
            print("file_name: ", file_name)

def buildCitcuit(file):
    f = open(file, "r")
    name = file.readLine()

    for line in file:
        print(line)
if __name__ == '__main__':
    readFiles()
