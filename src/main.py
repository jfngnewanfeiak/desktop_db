import os
import sys
import pathlib

sys.path.append(os.environ.get("MQTT_DB_MODULE_PATH"))
# from mqtt_interface_pub import MQTT_PUB
from mqtt_interface_sub import MQTT_SUB
from postgresql import POSTGRESQL

# DB 設定
DB = POSTGRESQL()
DB.setting_connection(host='localhost',user='postgres',database='sensor_db',password=os.environ.get("POSTGRE_PASS"))
DB.connect_DB()
print("connected DB!!!")

def callback(msg):
    msg = msg.split("/")
    DB.exec_update(f"insert into sensor_tb values({msg[1]},{msg[0]})")

if __name__ == "__main__":

    # MQTT 設定
    sub = MQTT_SUB()
    sub.sub_run(broker_ip='broker.emqx.io',topic_name='topic/AM2320',cb=callback)
    try:
        while True:
            pass
    except KeyboardInterrupt as KI:
        print(KI)