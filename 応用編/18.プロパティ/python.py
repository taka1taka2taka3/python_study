#property関数
class PropertyTest(object):

    def __init__(self, url):
        self._url = url

    def get_url(self):
        print('-- get_url --')
        return self._url

    url = property(get_url)


prop = PropertyTest('https://www.python-izm.com/')

print(prop.url)


class PropertyTest(object):

    def __init__(self, url):
        self._url = url

    def get_url(self):
        print('-- get_url --')
        return self._url

    def set_url(self, url):
        print('-- set_url --')
        self._url = url

    def del_url(self):
        del self._url

    url = property(get_url, set_url, del_url, 'url Property')


prop = PropertyTest('https://www.python-izm.com/')

prop.url = 'python-izm'

print(prop.url)


class PropertyTest(object):

    def __init__(self, scheme, host):
        self.schema = scheme
        self.host = host

    def get_url(self):
        return('{}://{}/'.format(self.schema, self.host))

    url = property(get_url)


prop = PropertyTest('https', 'www.python-izm.com')

print(prop.url)



#propertyデコレータ
class PropertyTest(object):

    def __init__(self, url):
        self._url = url

    @property
    def url(self):
        print('-- get_url --')
        return self._url


prop = PropertyTest('https://www.python-izm.com/')

print(prop.url)


class PropertyTest(object):

    def __init__(self, url):
        self._url = url

    @property
    def url(self):
        print('-- get_url --')
        return self._url

    @url.setter
    def url(self, url):
        print('-- set_url --')
        self._url = url

    @url.deleter
    def url(self):
        del self._url


prop = PropertyTest('https://www.python-izm.com/')

prop.url = 'python-izm'

print(prop.url)


class PropertyTest(object):

    def __init__(self, scheme, host):
        self.schema = scheme
        self.host = host

    @property
    def url(self):
        return('{}://{}/'.format(self.schema, self.host))


prop = PropertyTest('https', 'www.python-izm.com')

print(prop.url)
