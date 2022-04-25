SDA_PIN = 23 # update this
SCL_PIN = 22 # update this

i2c = machine.I2C(sda=machine.Pin(SDA_PIN), scl=machine.Pin(SCL_PIN), freq=400000)
seesaw = StemmaSoilSensor(i2c)

# get moisture
moisture = seesaw.get_moisture()

# get temperature
temperature = seesaw.get_temp()