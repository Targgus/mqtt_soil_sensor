# main.py

from umqtt.robust import MQTTClient
import machine
import utime as time
import gc
from soil_sensor import StemmaSoilSensor

client = MQTTClient("esp32-01", "10.0.0.146")
pin5 = machine.Pin(0, machine.Pin.OUT)

i2c = machine.I2C(machine.Pin(5), machine.Pin(4))
seesaw = StemmaSoilSensor(i2c)

def checkwifi():
    while not sta_if.isconnected():
        time.sleep_ms(500)
        print(".")
        sta_if.connect()

def publish():
    count = 1
    while True:
        pin5.value(0)
        checkwifi()
        
        # moisture = seesaw.get_moisture()
        msg = "Hello There!"
        client.publish(b"test/testing", str(seesaw.get_moisture()))
        pin5.value(1)
        count = count + 1
        time.sleep(10)

client.reconnect()

publish()