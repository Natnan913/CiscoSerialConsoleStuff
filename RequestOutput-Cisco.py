import serial
import time

bitRate = 9600
ComputerPort = 'COM3'
timeout = 1

intendedSerialPort= serial.Serial(ComputerPort, bitRate, timeout)


def outputOfCommand(command):
 
    intendedSerialPort.write(command.encode() + b'\r\n') #used \r\n so the Cisco switch can tell that where the end of the command is.
    time.sleep(2)
    output = intendedSerialPort.read(4096)     
         
    return output.decode(errors='ignore')
 

environmentInfo = outputOfCommand('show env all')
print("Output of show env all:\n", environmentInfo)

versionInfo = outputOfCommand('show version')
print("Output of show version:\n", versionInfo)

interfacesStatus = outputOfCommand('show interfaces status')
print("show interfaces status:\n", interfacesStatus)

interfaceErrorStats =  outputOfCommand('show interfaces | include error|CRC')
print("show interfaces | include error|CRC:\n", interfaceErrorStats)

intendedSerialPort.close()