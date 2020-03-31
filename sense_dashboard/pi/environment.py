from sense_hat import SenseHat
import threading
import firebase_admin
from firebase_admin import credentials, firestore
import time

#const
COLLECTION = 'raspberry'
DOCUMENT = 'lector pi'

# firebase
cred = credentials.Certificate("../assets/config/firebase_admin.json")
firebase_admin.initialize_app(cred)

# connect to firestore
db = firestore.client()

# sensehat 
sense = SenseHat()
sense.set_imu_config(False, False, False)
sense.clear()

def get_set_value():
    # get value
    temprature = round(sense.get_temperature())
    pressure = round(sense.get_pressure())
    humidity = round(sense.get_humidity())

    t = temprature
    d = pressure 
    v = humidity 

    # SET VALUES IN FIREBASE
    pi_ref.update(
        {'enviroment': 
            {
                'temprature' : temprature,
                'pressure' : pressure,
                'humidity' : humidity
            }
        },
        )

    sense.show_message("temperature")
    sense.show_message(str(t), text_colour=[255, 100, 100])
    sense.show_message(str(t), text_colour=[255, 100, 100])
    sense.show_message("pressure")
    sense.show_message(str(d), text_colour=[255, 100, 100])
    sense.show_message("humidity")
    sense.show_message(str(v), text_colour=[255, 100, 100])
    print("tempature=", t, "pressure=", d, "humidity=", v)
    return [temprature, pressure, humidity]

# connect firestore
db = firestore.client()
pi_ref = db.collection(COLLECTION).document(DOCUMENT)

# app
while True:
    get_set_value()
    time.sleep(2)