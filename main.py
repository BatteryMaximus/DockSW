from db_functions import setupPG
from charger_commands import getBatSerial
from serial_functions import getSerial
import time

if __name__ == "__main__":
    ser = getSerial('/dev/ttyS0', 115200)

    while True:
        batSerial = getBatSerial(ser)
        getBatSerial(ser)
        time.sleep(2)


