from serial_functions import setupSerial


ser = setupSerial('/dev/ttyS0', 115200)


def getBatSerial(ser):
    command = "G000A;"
    ser.write(command.encode('utf-8'))
    
    response = ser.readline()
    batSerial =  response.decode('utf-8').strip()
    print("Received: ", batSerial) 
    

