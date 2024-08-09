import os
import sys
import pathlib

# sys.path.append('C:\Users\81802\python_ws\sensor_data_mqtt_db')
sys.path.append(os.environ.get("MQTT_DB_MODULE_PATH"))
print(os.environ.get("MQTT_DB_MODULE_PATH"))
print(os.environ.get("POSTGRE_PASS"))
from mqtt_interface_pub import MQTT_PUB
from mqtt_interface_sub import MQTT_SUB
from postgresql import POSTGRESQL