import serial
import time

intendedSerialPort= serial.Serial('COM3', 9600, timeout=1)

def outputOfCommand(command, wait=1) :
    intendedSerialPort.write(command.encode() + b'\r\n') #used \r\n so the Cisco switch can tell that where the end of the command is.
    time.sleep(wait)  #it needs to wait for output otherwise the command comes out incorrectly. Same reason why I've kind of spammed "time.sleep" below.  
    output = ser.read(4096)               
    return output.decode(errors='ignore')

versionInfo = outputOfCommand('show version')
print("Output of show version:\n", versionInfo)

time.sleep(1) 

interfacesStatus = outputOfCommand('show interfaces status')
print("show interfaces status:\n", interfacesStatus)

time.sleep(1) 
interfaceErrorStats =  outputOfCommand('show interfaces | include error|CRC')
print("show interfaces | include error|CRC:\n", interfaceErrorStats)

ser.close()