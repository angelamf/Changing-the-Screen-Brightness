from os import system
from serial import Serial

portaSerial = Serial('COM4', 9600)
while True:
    intensidade = int(portaSerial.readline().decode())
    intensidade = int(intensidade*100/1024)
    print(intensidade)
    system(f'powercfg -setacvalueindex 381b4222-f694-41f0-9685-ff5bb260df2e 7516b95f-f776-4464-8c53-06167f40cc99 aded5e82-b909-4619-9949-f5d71dac0bcb {intensidade}')
    system('powercfg -s 381b4222-f694-41f0-9685-ff5bb260df2e')
