import json

from lazyjson import SafeJSON, JSONPassthroughEncoder


def test_encode_basic():
    o = {'hello': [1, 5.5, 'whee']}
    assert json.dumps(o) == JSONPassthroughEncoder().encode(o)


def test_encode_passthrough_alone():
    st = '"{"go": ["away", 6]}"'
    pt = SafeJSON(st)
    assert JSONPassthroughEncoder().encode(pt) == st


def test_encode_passthrough_embedded():
    o = {'root': [SafeJSON('{"go": ["away", 6]}')]}
    o2 = {'root': [{'go': ['away', 6]}]}
    a = JSONPassthroughEncoder().encode(o)
    b = json.dumps(o2)
    assert a == b
