from os import system, remove
from serial import Serial
import serial.tools.list_ports

SERIAL_PORT = serial.tools.list_ports.comports()[-1]  # Pega a última porta Serial da lista ativa
BAUD_RATE = 9600
connection = Serial(SERIAL_PORT.device, BAUD_RATE)


def getGUID(f, key):
    for line in f:
        if key in line:
            return line[line.index(': ') + 2:line.rindex(' (') - 1]


def getValue():
    return int(int(connection.readline().decode()) * 100 / 1024)


def setBrightness(value):
    system('powercfg -q > a.txt')
    file = open('a.txt', 'r')
    a = getGUID(file, 'Esquema de Energia')
    b = getGUID(file, '(V')
    c = getGUID(file, '(Brilho do v')
    remove('a.txt')
    system(f'powercfg -setacvalueindex {a} {b} {c} {value}')
    system(f'powercfg -s {a}')


# Corpo Principal
while True:
    val = getValue()
    setBrightness(val)
