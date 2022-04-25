## Equipment List
1. [Feather HUZZAH w/ ESP8266 Wifi](https://www.adafruit.com/product/3213)
2. [Adafruit STEMMA Soil Sensor](https://www.adafruit.com/product/4026)
3. [JST PH 4-Pin Female Socket Cable](https://www.adafruit.com/product/3950)
4. [USB Cable - USB A to Micro B](https://www.adafruit.com/product/592)
5. [5V 1A USB Power Supply](https://www.adafruit.com/product/501)

</br>

## Get Started

</br>

Create venv for Python

```
mkdir soilsensor
cd soilsensor
python -m venv venv
source venv/bin/activate
```

Install libraries
 
```
(venv) pip install esptool
(venv) pip install adafruit-ampy
```

Download latest .bin firmware [here](https://micropython.org/download/esp8266-1m/) for adafruit board

Determine serial port on MacOS

```
(venv) ls /dev/tty.*
```

Erase ESP8266 and flash new firmware (replace serial with result from last step)

```
(venv) esptool.py --port serial erase_flash

(venv) esptool.py --port serial --baud 115200 write_flas --flash_size=detect 0 esp8266-1m-20220117-v1.18.bin
```

Reset the board using button or unplugging and plugging back in

Use MacOS's screen to log in

```
(venv) screen serial 115200
```
Hit "Enter" until >>> appears

Run test code 

```
>>>import machine

>>>redled=machine.Pin(0, machine.Pin.OUT)

>>>redled.value(0)
>>>redled.value(1)
```

How to upload files

```
(venv) ampy --port serial put file_name.py
```
</br>

## Soil Moisture MQTT Program
</br>

Prep and install MQTT (resource [here](https://github.com/gloveboxes/ESP32-MicroPython-BME280-MQTT-Sample/blob/master/Micropython.md))
```
import upip
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect("Wifi SSID", "Wifi password")

upip.install('micropython-umqtt.simple')
upip.install('micropython-umqtt.robust')
```
Update line 4 in boot.py with wifi SSID and Password

Update line 9 in main.py to point to MQTT Broker IP

Upload the following to feather:
- boot.py
- main.py
- soil_sensor.py
- seesaw.py

Connect soil sensor to 3V3, GND, SLC, and SDA pins like [this diagram](https://learn.adafruit.com/adafruit-stemma-soil-sensor-i2c-capacitive-moisture-sensor/python-circuitpython-test)

Reboot Feather. Wait for red led to turn off, indicating publisher has successfully started.

Start subscriber on Broker or additional accessory. If using mosquitto:

```
mosquitto_sub -h localhost -t test/testing
```

Place sensor in soil and observe values. Dry soil should be around 300. Wet soil should be around 500. 