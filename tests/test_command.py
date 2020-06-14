import json

from toad_sp_command import command, protocol


def test_parse_message():
    topic = protocol.SHORT_TOPIC
    payload = json.dumps(
        {
            "subtopics": ["sp_g0", "sp_w.r3.c5", "row/1", "column/2"],
            "payload": '{"status": 1}',
        }
    )
    ips = {
        "sp_g0": "0.0.0.1",
        "sp_w.r1.c1": "0.0.0.2",
        "sp_w.r3.c2": "0.0.0.3",
    }
    targets, status, err = command.parse_message(topic, payload, ips)
    print(f"Targets:\t{targets}\nStatus:\t{status}\nError:\t{err}")
    assert err == "" and status and len(targets) == 3
