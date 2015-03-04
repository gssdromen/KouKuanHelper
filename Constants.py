# coding:UTF-8

class Constants(object):
    def __init__(self):
        self._baseurl = 'https://vfs.saicfc.com'
        # baseUrl = 'https://10.116.8.65:8002'

        # baseUrl = 'http://10.116.15.65:9003'
        # self._baseurl = "https://10.116.8.65:8002"

    @property
    def baseurl(self):
        """I'm the 'x' property."""
        return self._baseurl

    @baseurl.setter
    def baseurl(self, value):
        self._baseurl = value

    @baseurl.deleter
    def baseurl(self):
        del self._baseurl

