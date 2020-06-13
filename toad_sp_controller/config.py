from os import path
import configparser

_config = configparser.ConfigParser()
_config_path = path.join(
    *path.split(path.dirname(path.abspath(__file__)))[:-1], "config", "config.ini"
)
_config.read(_config_path)

_command_config = _config["COMMAND"]
_etcd_config = _config["ETCD"]
_logger_config = _config["LOGGER"]
_mqtt_config = _config["MQTT"]
_workspace_config = _config["WORKSPACE"]

# Configuration variables
# COMMAND
SLEEP_TIME = float(_command_config.get("sleep_time"))
# ETCD
ETCD_HOST = _etcd_config.get("host")
ETCD_PORT = int(_etcd_config.get("port"))
ETCD_KEY = _etcd_config.get("key")
# Logger
LOGGER_VERBOSE = _logger_config.getboolean("verbose")
# MQTT
MQTT_BROKER_HOST = _mqtt_config.get("broker_host")
MQTT_BROKER_PORT = int(_mqtt_config.get("broker_port"))
MQTT_RESPONSE_TIMEOUT = int(_mqtt_config.get("response_timeout"))
# Workspace
COLUMNS_POR_ROW = int(_workspace_config.get("columns_per_row"))
ROWS_PER_COLUMN = int(_workspace_config.get("rows_per_column"))
