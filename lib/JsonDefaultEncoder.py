from json import JSONEncoder


class JsonDefaultEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__