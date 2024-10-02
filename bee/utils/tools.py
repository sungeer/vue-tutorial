import json


class BaseResponse:

    def __init__(self):
        self.status = True
        self.error_code = None
        self.message = None
        self.data = None

    def to_dict(self):
        return self.__dict__


class JsonExtendEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, BaseResponse):
            return obj.__dict__
        return super().default(obj)


def dict_to_json(data):
    if not data:
        data = {}
    return json.dumps(data, cls=JsonExtendEncoder)


def dict_to_json_ea(data=None):
    return json.dumps(data, cls=JsonExtendEncoder, ensure_ascii=False, indent=4)


def json_to_dict(json_data):
    return json.loads(json_data)
