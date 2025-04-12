from db_functions import setupPG
from charger_commands import getBatSerial
from serial_functions import getSerial
import time

if __name__ == "__main__":
    ser = getSerial('/dev/ttyS0', 115200)

    while True:
        batSerial = int(getBatSerial(ser))
        print('Battery Serial Number: {%s}', batSerial)
        time.sleep(2)


