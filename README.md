# toad_sp_command
<!--[![Build Status](https://travis-ci.com/morelab/toad_sp_command.svg?branch=master)](https://travis-ci.com/morelab/toad_sp_command)
[![codecov](https://codecov.io/gh/morelab/toad_sp_command/branch/master/graph/badge.svg)](https://codecov.io/gh/morelab/toad_sp_command)
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)
[![black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
-->
Smart Plug controller component for the IoToad paltform

## Development requirements

The development dependencies are listed in `requirements_dev.txt` and should
be installed alongside `requirements.txt`.

There are two services that need to be started before running tests: MQTT and ETCD.

### MQTT

The following shell command creates and runs a mosquitto container.

```bash
docker run \
--name=mosquittoc \
--publish 1883:1883 \
--network=host \
toke/mosquitto\
"
```

### ETCD

> **Note**: The ETCD database might need to be populated

Create a permanent storage folder:

```bash
mkdir -p $HOME/.var/lib
```

And run the ETCD docker container:

```bash
VOL_DIR="$HOME/.var/lib"
ETCD_ADDR="127.0.0.1"
ETCD_DIR="${VOL_DIR}/etcd"

docker run \
--name=etcdc \
--network=host \
--mount type=bind,src=${ETCD_DIR},dst=/etcd-data \
quay.io/coreos/etcd \
/usr/local/bin/etcd \
--data-dir=/etcd-data --name etcd_node \
--initial-advertise-peer-urls http://${ETCD_ADDR}:2380 --listen-peer-urls http://0.0.0.0:2380 \
--advertise-client-urls http://${ETCD_ADDR}:2379 --listen-client-urls http://0.0.0.0:2379 \
--initial-cluster etcd_node=http://${ETCD_ADDR}:2380 \
"
```


