import Adafruit_DHT

# Sensor should be set to Adafruit_DHT.DHT11,
sensor = Adafruit_DHT.DHT11

#GPIO pin 4 as per BCM Numbering and 7 as per board pin numbering
sensor_pin = 4

# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
else:
    print('Failed to get reading. Try checking the pin numbering and connections!')
