import wiotp.sdk.device
import time
import random
myConfig = { 
    "identity": {
        "orgId": "l0lyjx",
        "typeId": "AApp1",
        "deviceId":"12345"
    },
    "auth": {
        "token": "12345678"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    tanklv=random.randint(-20,125)
    lightint=random.randint(0,100)
    myData={'WaterTankLevel':tanklv, 'LightIntensity':lightint}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s", myData)
    client.commandCallback = myCommandCallback
    time.sleep(2)
client.disconnect()

