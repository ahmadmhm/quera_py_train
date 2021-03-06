class Proxy:
    def __init__(self, obj):
        self._obj = obj
        self.last_invok = []
        self.before = ''
        self.log = {}

    def __getattr__(self, attr):
        self.last_invok.append(attr)
        if not attr in self.log:
            self.log[attr] = 1
        else:
            self.log[attr] +=1
        try:
            return getattr(self._obj, attr)
        except Exception:
            self.last_invok = self.last_invok[:-1]
            raise Exception('No Such Method')

    def last_invoked_method(self):
        if len(self.last_invok)>0:
            return self.last_invok[-1]
        raise Exception('No Method Is Invoked')

    def count_of_calls(self, method_name):
        if method_name in self.log:
            return self.log[method_name]
        return 0
        pass

    def was_called(self, method_name):
        return method_name in self.log
        pass

class Radio():
    def __init__(self):
        self._channel = None
        self.is_on = False
        self.volume = 0

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value

    def power(self):
        self.is_on = not self.is_on
"""
class Proxy:
    def __init__(self, obj):
        self._obj = obj
        self.last_invoked = ''
        self.count = {}

    def last_invoked_method(self):
        if self.last_invoked == '':
            raise Exception('No Method Is Invoked')
        else:
            return self.last_invoked

    def count_of_calls(self, method_name):
        if method_name in self.count.keys():
            return self.count[method_name]
        else:
            return 0

    def was_called(self, method_name):
        if method_name in self.count.keys() and self.count[method_name] > 0:
            return True
        else:
            return False

    def __getattr__(self, attr):
        if attr in dir(self._obj):
            self.last_invoked = attr
            if attr in self.count.keys():
                self.count[attr] += 1
            else:
                self.count[attr] = 1
            return getattr(self._obj, attr)
        else:
            raise Exception("No Such Method")


class Radio():
    def __init__(self):
        self._channel = None
        self.is_on = False
        self.volume = 0

    def get_channel(self):
        return self._channel

    def set_channel(self, value):
        self._channel = value

    def power(self):
        self.is_on = not self.is_on
"""