import serial
import time
from openpyxl import load_workbook

ser = serial.Serial('COM3', 9600, timeout=1)

def sendCommand(command, wait=1) :
    ser.write(command.encode() + b'\r\n')
    time.sleep(wait)  #will wait for the switch to return output   
    output = ser.read(4096)               
    return output.decode(errors='ignore')

version = sendCommand('show version')
print("Output of show version:\n", version)

time.sleep(1) 

interfaceStatus = sendCommand('show interfaces status')
print("show interfaces status:\n", interfaceStatus)

time.sleep(1) 
intErrors = sendCommand('show interfaces | include error|CRC')
print("show interfaces | include error|CRC:\n", intErrors)

ser.close()