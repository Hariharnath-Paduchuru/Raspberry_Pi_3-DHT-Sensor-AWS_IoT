import os
import sys
import AWSIoTPythonSDK
import json
sys.path.insert(0, os.path.dirname(AWSIoTPythonSDK.__file__))
# Now the import statement should work
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import Adafruit_DHT
import logging
import time
import getopt
import datetime

#Change it to 11 or 22 based on your sensor
DHT_TYPE = Adafruit_DHT.DHT11

#GPIO pin 4 as per BCM Numbering and 7 as per board pin numbering
DHT_PIN  = 4 


# Custom MQTT message callback
def customCallback(client, userdata, message):
	print("Received a new message: ")
	print(message.payload)
	print("from topic: ")
	print(message.topic)
	print("--------------\n\n")


# Modify these Parameters according to your AWS IOT account
useWebsocket = False
host = "xxxxxxxx.amazonaws.com"
rootCAPath = "root-CA.pem"
certificatePath = "xxxxx-certificate.pem.crt"
privateKeyPath = "xxxxx-private.pem.key"
Client_ID = "RaspberryPi"
AWS_IOT_MY_THING_NAME = "Your Thing Name"


# Configure logging
logger = None
if sys.version_info[0] == 3:
	logger = logging.getLogger("core")  # Python 3
else:
	logger = logging.getLogger("AWSIoTPythonSDK.core")  # Python 2
logger.setLevel(logging.DEBUG)
streamHandler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

# Initialize AWSIoTMQTTClient
myShadowClient = None
if useWebsocket:
	myShadowClient = AWSIoTMQTTClient(Client_ID, useWebsocket=True)
	myShadowClient.configureEndpoint(host, 443)
	myShadowClient.configureCredentials(rootCAPath)
else:
	myShadowClient = AWSIoTMQTTClient(Client_ID)
	myShadowClient.configureEndpoint(host, 8883)
	myShadowClient.configureCredentials(rootCAPath, privateKeyPath, certificatePath)

# AWSIoTMQTTClient connection configuration
'''
myShadowClient.configureAutoReconnectBackoffTime(1, 32, 20)
myShadowClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myShadowClient.configureDrainingFrequency(2)  # Draining: 2 Hz
'''
myShadowClient.configureConnectDisconnectTimeout(10)  # 10 sec
myShadowClient.configureMQTTOperationTimeout(5)  # 5 sec

# Connect and subscribe to AWS IoT
myShadowClient.connect()

#myShadowClient.subscribe("dht11", 1, customCallback)
time.sleep(2)

# Publish to the topic in a loop
#this is the topic to update to the thing shadow
#topic="$aws/things/"+AWS_IOT_MY_THING_NAME+"/shadow/update"

#To test your topic use this
topic="awsiot/dht11"

#modify this delay as per your need
delay_sec = 10
sensor_id = 'DHT11_xxx'
#myShadowClient .subscribe(topic+"/delta", 1, customCallback)
try:
	while True:
		humidity, temperature = Adafruit_DHT.read(DHT_TYPE, DHT_PIN)
		timestamp = datetime.datetime.now()
		if humidity is not None and temperature is not None:
			print('\n--------------------------------------------------------')
			print(" Output is here")
			print(' Time: {} \n'.format(timestamp))
			print(' Temperature: {} C  Humidity: {} timestamp: {}'.format(temperature,humidity,timestamp))
			msg = ' "Pi_timestamp": "{}","Sensor": "{:s}", "Temperature": "{}","Humidity": "{}" '.format(timestamp,sensor_id, temperature,humidity)
			msg = '{'+msg+'}'
			#payload={"state":{"reported": {"timestamp": timestamp,"Temperature": temperature, "Humidity": humidity }}}
			#payload=json.dumps(payload)
			print(msg)
			print('--------------------------------------------------------\n')
			status=myShadowClient.publish(topic, msg, 1)
			if(status):
				print("Updated " +str(status))
			print('Sleeping for '+ str(delay_sec)+' ...')
			time.sleep(delay_sec)
		else:
			pass
except KeyboardInterrupt:
	pass
finally:
	print('Exiting the loop');
	myShadowClient.disconnect()
	print('Disconnected from AWS')
