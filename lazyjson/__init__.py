import json

class JSONValue:
    __slots__ = ['v']
    def __init__(self, v):
        self.v = v

    def parse(self):
        return json.loads(self.v)


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, JSONValue):
            return o
        return super().default(o)

    def iterencode(self, o, _one_shot=False):
        if isinstance(o, JSONValue):
            return o.v
        return super().iterencode(o, _one_shot=_one_shot)

