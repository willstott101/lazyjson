import json, os

from lazyjson import SafeJSON, SafeJSONFile, JSONPassthroughEncoder


def test_pi():
    st = os.stat('tests/pi.json')
    meta = {
        "size": st.st_size,
        "mtime": st.st_mtime,
    }
    with open('tests/pi.json') as f:
        doc = dict(content=SafeJSONFile(f), **meta)
        res = JSONPassthroughEncoder().encode(doc)

    with open('tests/pi.json') as f:
        assert json.loads(res) == dict(content=json.load(f), **meta)

def test_pi_iter():
    st = os.stat('tests/pi.json')
    meta = {
        "size": st.st_size,
        "mtime": st.st_mtime,
    }
    with open('tests/pi.json') as f:
        doc = dict(content=SafeJSONFile(f), **meta)
        for t in JSONPassthroughEncoder().iterencode(doc):
            assert len(t) <= 2048

def test_my():
    st = os.stat('tests/my.json')
    content = open('tests/my.json').read()
    meta = {
        "size": st.st_size,
        "mtime": st.st_mtime,
    }
    doc = dict(content=SafeJSON(content), **meta)
    res = JSONPassthroughEncoder().encode(doc)

    assert json.loads(res) == dict(content=json.loads(content), **meta)

