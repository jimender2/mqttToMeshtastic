#!/usr/bin/env python3
from paho.mqtt import client as mqtt_client

from random import uniform
import time
import json
import random


broker = "mqtt.meshtastic.org"
port = 1883
topic = "$SYS/broker/connection/msh/US/OH"
# Generate a Client ID with the subscribe prefix.
client_id = f"subscribe-{random.randint(0, 100)}"
username = "meshdev"
password = "large4cats"


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(mqtt_client.CallbackAPIVersion.VERSION1, client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


client = connect_mqtt()
while True:
    randNumber = uniform(20.0, 21.0)
    client.publish("$SYS/broker/connection/msh/US/OH", json.dumps({"test": randNumber}))
    print("Just published %s to topic %s" % (randNumber, topic))
    time.sleep(1)
