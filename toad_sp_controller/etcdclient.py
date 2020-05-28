"""Helper submodule for operations on ETCD."""
from typing import Dict

import etcd  # import python-ectd module


def get_cached_ips(host: str, port: int, key: str) -> Dict[str, str]:
    """
    Retrieved previously known IP addresses of smartplugs.

    :param host: ETCD host
    :param port: ETCD port
    :param key: parent key of all the cached ID->IP association
    :return: dict with smartplug IDs as keys and IPs as values
    """
    client = etcd.Client(host=host, port=port)
    ips = {}
    parent: etcd.EtcdResult = ...
    try:
        parent = client.read(key)
    except etcd.EtcdKeyNotFound:
        return {}
    for child in parent.children:
        k = child.key.split("/")[-1]
        ips[k] = child.value
    return ips
