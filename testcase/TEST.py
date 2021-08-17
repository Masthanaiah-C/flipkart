import serial
import time
COM_PORT = 'com15'
REVOLUTION = 100
INSTRUCTIONS = [[[1,3,1,5,1,4,1,8],[8,1,7,1,7,1,8,0]],
                [[1,3,1,5,1,4,1,8],[9,1,8,1,8,1,9,0]],
                [[1,4,1,5,1,3,1,8],[9,1,8,1,8,1,9,0]],
                [[1,4,1,5,1,3,1,8],[8,1,7,1,7,1,8,0]]]


ArduinoUnoSerial = serial.Serial(COM_PORT,9600) #look at the bottom of the arduino ide to get the com port
for i in INSTRUCTIONS:
    for j in range(len(i[0])):
        x='1'+str(INSTRUCTIONS[i][0][j])+','+str((INSTRUCTIONS[i][0][j])*REVOLUTION)+'\n'
        ArduinoUnoSerial.write(bytes(x, 'utf-8'))
        time.sleep(0.10)