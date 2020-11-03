import requests
import json
import functools


def check_for_204(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except json.JSONDecodeError:
            return False

    return inner()


# our metaclass
class CheckResponseMeta:
    # overriding __new__ method
    def __new__(cls, name, bases, dct):
        for attr in dct:
            value = dct[attr]
            if callable(value):
                dct[attr] = check_for_204(value)
        return super().__new__(cls, name, bases, dct)


class BrixAPI:

    __metaclass__ = CheckResponseMeta

    def get_response(self):
        try:
            url = 'https://httpstat.us/204'
            resp = requests.get(url)
            print(resp.status_code)
            print(resp.text)
            # error, if there no response
            # status code 204
            data = json.loads(resp.text)
            print(data)
            return data

        except json.decoder.JSONDecodeError as err:
            print("there is no response, I cannot convert data into dict")


# satish tests
def test_getProject_By_Model_Year2():

    t = BrixAPI()
    response = t.get_response()
    if response:
        return_code = response['returncode']
        if return_code == 1:
            print("Project Found By Year:")
        else:
            print("Invalid Year key OR Project not available")


test_getProject_By_Model_Year2()
