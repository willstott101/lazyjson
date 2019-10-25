import json
import pytest

from lazyjson import JSONValue, JSONEncoder


def test_encode_basic():
    o = {'hello': [1, 5.5, 'whee']}
    assert json.dumps(o) == JSONEncoder().encode(o)


def test_encode_passthrough_alone():
    st = '"{"go": ["away", 6]}"'
    pt = JSONValue(st)
    assert JSONEncoder().encode(pt) == st


@pytest.mark.xfail
def test_encode_passthrough_embedded():
    o = {'root': [JSONValue('{"go": ["away", 6]}')]}
    o2 = {'root': [{'go': ['away', 6]}]}
    a = JSONEncoder().encode(o)
    b = json.dumps(o2)
    assert a == b
