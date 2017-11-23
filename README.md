# Upload DHT11 Data to AWS IoT Using Raspberry Pi 3 with MQTT Protocol
Upload the Temperature and humidity values to AWS IoT Using Raspberry Pi 3

## Project Overview

This Project will help you setup the Raspberry pi 3 with DHT Sensor and upload the data to AWS IoT with MQTT protocol.

Raspberry pi 3 is used to connect and fetch the values from the DHT11,Temperature and Humidity sensor. It also is used to connect  and push the data to the AWS cloud in Json format using MQTT protocol.


## Flow Chart

![FlowChart](https://user-images.githubusercontent.com/29800208/32888257-acb9752e-caec-11e7-8dde-f3c26aeef6e7.png)


## Basic Steps:

1.  Basic Installation setup of Raspberry Pi 3
2.  Connect the Hardware component (DHT11) to the Raspberry Pi 3
3. AWS account creation
4. Configuring the AWS IoT Services
5. Programming the Raspberry Pi


## Requirements

### Hardware

1. Raspberry pi 3 (with Raspbian Jessie OS)
2. Micro-USB cable for power
3. Breadboard
4. DHT11 temperature and humidity sensor
5. Jumper wires
6. HDMI cable/ LAN Cable

### Software

- Python

```sh

sudo apt-get update

sudo apt-get install python3

```

- Adafruit Python DHT Sensor Library
  - This is a python library for reading DHT series of temperature and humidity on raspberry pi. Reference code is available [here](https://github.com/adafruit/Adafruit_Python_DHT)

```sh

sudo apt-get update

sudo apt-get install python-dev

sudo apt-get install python-rpi.gpio

```


```sh

git clone https://github.com/adafruit/Adafruit_Python_DHT.git

cd Adafruit_Python_DHT

sudo apt-get update

sudo apt-get install build-essential python-dev python-openssl

sudo python setup.py install

```

- AWS IoT Device SDK for Python

```sh

pip install AWSIoTPythonSDK

```

- Clone the Git repository

```sh

git clone https://github.com/hariharnath/Raspberry_Pi_3-DHT-Sensor-AWS_IoT

```

- Amazon Web Services AWS IoT

   Register and login through AWS console [here](https://aws.amazon.com/). Create a free account. Now you can access all free tier amazon web services.

### Step 1:

- Setup the Raspberry pi as per the initial setup mentioned [here](https://raspberrypihq.com/booting-the-raspberry-pi-for-the-first-time/)


### Step 2:

- Connecting Raspberry pi with DHT11 sensor. Make the connections as mentioned in the below pictures.
![Types of DHT11 sensors](http://www.circuitbasics.com/wp-content/uploads/2015/12/DHT11-Pinout-for-three-pin-and-four-pin-types-2.jpg)

![3 pin type DHT Sensor connection](http://www.circuitbasics.com/wp-content/uploads/2015/12/How-to-Setup-the-DHT11-on-the-Raspberry-Pi-Three-pin-DHT11-Wiring-Diagram.png)


![4 pin type DHT Sensor Connection](http://www.circuitbasics.com/wp-content/uploads/2015/12/How-to-Setup-the-DHT11-on-the-Raspberry-Pi-Four-pin-DHT11-Wiring-Diagram.png)


- Power up your raspberry pi, take a breadboard, dht11 sensor and some jumper wires. The resistor is a 10K Ohm pull up resistor connected between the Vcc and signal lines.
  - Signal Pin is connected to the GPIO pin 4 of pi
  - Negative pin of sensor is connected to GPIO pin 6 of pi
  - Vcc pin of sensor is connected  to GPIO pin 2 of pi
  
![Raspberry pi pinout](https://www.raspberrypi-spy.co.uk/wp-content/uploads/2012/06/Raspberry-Pi-GPIO-Layout-Model-B-Plus-rotated-2700x900.png)

   Test: To check connection a sample program, Run

```sh

sudo python testDHT11.py

```

   The output should show temperature in degree Celsius and humidity percentage readings in console every 5 seconds iteratively.


### Step 3:

1. Create an account in AWS [here](https://aws.amazon.com)
2. Follow the steps mentioned [here](http://docs.aws.amazon.com/iot/latest/developerguide/iot-console-signin.html)
3. While Creating policies, try to allow iot:\* for learning purpose which means we are allowing all the traffic.
4. Download all the certificates and put them onto the Raspberry pi using WinSCP for Windows in the same folder of the cloned git repository for easy purpose, if not you should change the file path in the code.


### Step 4:

1. Open the test tab of the AWS IoT service
2. Click on subscribe to a topic and enter the topic as &quot;awsiot/dht11&quot; without quotes.
3. Take a note of this topic.


### Step 5:

1. Open the console in Raspberry pi, Clone the git Repo and run the code

```sh
cd

git clone https://github.com/hariharnath/Raspberry_Pi_3-DHT-Sensor-AWS_IoT

ls Raspberry_Pi_3-DHT-Sensor-AWS_IoT

sudo nano PublishTempToAWS.py

```

   Check if the topic mentioned here is same as you have subscribed, If not modify the file and click on ctrl + o and ctrl + x

```sh

sudo python PublishTempToAWS.py

```

   You should see the log in the console

   Check the aws subscribed topic in the test tab of AWS IoT , you should see the messages being published.
