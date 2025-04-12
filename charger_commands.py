
def getBatSerial(ser):
    command = "G000A;"
    ser.write(command.encode('utf-8'))
    response = ser.readline()
    batSerial =  response.decode('utf-8').strip()
    return batSerial
