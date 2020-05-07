from os import popen, remove
from sys import platform
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
    if 'win' in platform:
        popen('powercfg -q > a.txt')
        file = open('a.txt', 'r')
        a = getGUID(file, 'Esquema de Energia')
        b = getGUID(file, '(V')
        c = getGUID(file, '(Brilho do v')
        remove('a.txt')
        popen(f'powercfg -setacvalueindex {a} {b} {c} {value}')
        popen(f'powercfg -s {a}')
    elif 'linux' in platform:
        a = popen("xrandr -q | grep ' connected' | head -n 1 | cut -d ' ' -f1").read().rstrip('\n')
        print(f'xrandr --output {a} --brightness {value / 100:.2f}')
        popen(f'xrandr --output {a} --brightness {value / 100:.2f}')


# Corpo Principal
while True:
    val = getValue()
    setBrightness(val)
