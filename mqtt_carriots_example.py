#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Client paho-mqtt CarriotsMqttServer
# mqtt_carriots_example.py
import paho.mqtt.publish as publish
from json import dumps
from ssl import PROTOCOL_TLSv1


class CarriotsMqttClient():
    host = 'mqtt.carriots.com'
    port = '1883'

    def __init__(self, auth, tls=None):
        self.auth = auth
        self.topic = '%s/streams' % auth['username']
        if tls:
            self.tls = tls
            self.port = '8883'

    def publish(self, msg):
        try:
            publish.single(
                topic=self.topic, 
                payload=msg, 
                hostname=CarriotsMqttClient.host, 
                auth=self.auth, 
                tls=self.tls, 
                port=CarriotsMqttClient.port
            )
        except Exception, ex:
            print ex


if __name__ == '__main__':
    auth = {'username': 'YOUR_APIKEY_HERE', 'password': ''}
    # You must download ca_certs.crt from https://www.carriots.com/tls/ca_certs.crt for use TLSv1
    tls_dict = {'ca_certs': 'ca_certs.crt', 'tls_version': PROTOCOL_TLSv1}
    msg_dict = {'protocol': 'v2', 'device': 'YOUR_ID_DEVELOPER_DEVICE_HERE', 'at': 'now', 'data': {'key': 'value'}}
    client_mqtt = CarriotsMqttClient(auth=auth)                     # non ssl version
    #client_mqtt = CarriotsMqttClient(auth=auth, tls=tls_dict)      # ssl version
    client_mqtt.publish(dumps(msg_dict))
