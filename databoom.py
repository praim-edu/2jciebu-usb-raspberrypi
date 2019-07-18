import paho.mqtt.client as mqtt
import ssl
import json




class Databoom:
    def __init__(self, appid, psw, cid):
        self.client = mqtt.Client()
        #client = mqtt.Client(client_id="y1Bk-0ukkus6pz8",userdata=settings,protocol=mqtt.MQTTv311,transport="tcp")
        self.client = mqtt.Client(client_id=cid,protocol=mqtt.MQTTv311,transport="tcp")

        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_publish = self.on_publish
        print ("connecting")
        
        self.client.username_pw_set(appid,psw)
        self.client.connect("mqtt.databoom.com",1883,60)

    def on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc)) 
        #debug result
        return

    def on_message(client, userdata, msg):
        #debug
        #print(msg.topic+" "+str(msg.payload))
        return

    def on_publish(client,userdata,result):
        print(result.topic+" "+str(result.payload))
        #debug result
        return
