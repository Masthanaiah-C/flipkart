import serial
import time
COM_PORT = 'COM4' #import
REVOLUTION = 100 
INSTRUCTIONS = [[1,3,1,5,1,4,1,8],[8,1,7,1,7,1,8,0]]

ArduinoUnoSerial = serial.Serial(COM_PORT,9600) #look at the bottom of the arduino ide to get the com port

for j in range(len(INSTRUCTIONS[0])):
        x='1,'+str(INSTRUCTIONS[0][j])+','+str((INSTRUCTIONS[1][j])*REVOLUTION)+'\n'
        ArduinoUnoSerial.write(bytes(x, 'utf-8'))
        time.sleep(0.2*INSTRUCTIONS[1][j])
        # x ='1,1,8\n'