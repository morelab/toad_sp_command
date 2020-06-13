import etcd
import pytest
import uuid

from tests import ETCD_HOST, ETCD_PORT, ETCD_KEY
from toad_sp_command import etcdclient


class TmpClient(etcd.Client):
    expected = {
        "w.r3.c4": "0.0.0.1",
        "w.r1.c1": "0.0.0.2",
        "w.r3.c2": "0.0.0.3",
    }

    def __init__(self, host, port, key):
        super().__init__(host, port)
        self.key = key


@pytest.fixture
def tmp_client():
    key = f"{ETCD_KEY}/{uuid.uuid4()}"
    client = TmpClient(ETCD_HOST, ETCD_PORT, key)
    for k, v in client.expected.items():
        client.write(f"{key}/{k}", v)
    yield client
    for k, v in client.expected.items():
        client.delete(f"{key}/{k}")


def test_get_smartplug_ids(tmp_client):
    ips = etcdclient.get_cached_ips(ETCD_HOST, ETCD_PORT, tmp_client.key)
    assert len(ips) == len(tmp_client.expected)
    for k, v in ips.items():
        assert k in tmp_client.expected and ips.get(k) == tmp_client.expected.get(k)
