# :mask: :coffee: :computer: [Quarentine Project](https://github.com/lucas26xd/Quarentine-Projects) #0 - Automatic brightness adjustment according to external brightness.
![GitHub author](https://img.shields.io/badge/author-angelamf_and_lucas26xd-ff0080?style=flat-square)
[![GitHub last commit](https://img.shields.io/github/last-commit/angelamf/Changing-the-Screen-Brightness?color=ff0080&style=flat-square)](../../commits/master)
![GitHub repo size](https://img.shields.io/github/repo-size/angelamf/Changing-the-Screen-Brightness?color=ff0080&style=flat-square)
[![GitHub license](https://img.shields.io/github/license/angelamf/Changing-the-Screen-Brightness?color=ff0080&style=flat-square)](LICENSE)
![GitHub top language](https://img.shields.io/github/languages/top/angelamf/Changing-the-Screen-Brightness?color=ff0080&style=flat-square)
![GitHub count language](https://img.shields.io/github/languages/count/angelamf/Changing-the-Screen-Brightness?color=ff0080&style=flat-square)
# :high_brightness: Automatic brightness adjustment according to external brightness from an LDR on an Arduino.

## ⚙ Behavior
#### Simple Python3 application that receives the external luminance values sent by the microcontroller via Serial.
#### An Arduino UNO with an LDR sensor was used,  connected to the analog port A0, as shown in the schematic below, connected to the computer.
![Schematic](https://www.aranacorp.com/wp-content/uploads/pr-sensor-scheme_bb.png)

#### To run the application, run the following command:
> python main.py

##### Logically the C code should be running on the Arduino connected to the computer.

## 📝 Comments
- On Windows, the script automatically takes the video information to control the computer screen brightness from a file.
- On Linux, the script takes the name of the active display automatically.


## 🚀 Tecnologies
#### We use [Python3](https://www.python.org/) in the desktop application and [C](https://www.learn-c.org/) in the application that will run on [Arduino](https://www.arduino.cc/). 

## 🔨 Dependencies
#### We use the library [pyserial](https://pypi.org/project/pyserial/) for communication between the Arduino and the computer.
#### To install this dependency you can use the following command:
> pip install pyserial

Make sure you have [pip](https://pypi.org/project/pip/) and [Python3](https://www.python.org/) installed on your computer.

Made with 💙, C and Python
