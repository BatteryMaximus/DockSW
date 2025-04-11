import serial
import time


def getSerial(serialPort, baudrate):
    ser = serial.Serial(
            port = serialPort,
            baudrate = baudrate,
            byteszie=serial.EIGHTBITS,
            parity=serial.PARITY_NONE,
            stobbits=serial.STOPBITS_ONE,
            timeout=1
            )
    print("Sleeping, to wait for initialization")
    time.sleep(2)
    return ser



