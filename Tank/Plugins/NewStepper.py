'''
Tools for preparing phantom input data file
'''

#from collections import defaultdict
#from progressbar import ProgressBar, Percentage, Bar, ETA
#import logging
#import operator
#import os
#import re
#import tempfile
#import tankcore

from itertools import cycle


class HttpAmmo(object):
    def __init__(self, uri, host, method):
        self.method = method
        self.uri = uri
        self.host = host
        self.proto = "HTTP/1.1"
        self.headers = []
        self.body = []

    def to_s(self):
        return "%s %s %s" % (self.method, self.uri, self.proto)


class AbstractMissileGenerator(object):
    def __iter__(self):
        return self

    def next(self):
        raise NotImplemented


class SimpleMissileGenerator(AbstractMissileGenerator):
    '''Generates ammo based on given sample'''
    def __init__(self, missile_sample):
        self.missile_sample = missile_sample

    def next(self):
        return self.missile_sample


class UriStyleMissileGenerator(AbstractMissileGenerator):
    '''Generates GET ammo based on given URI list'''
    def __init__(self, host, uri_list):
        self.missiles = cycle([HttpAmmo(uri, host, "GET") for uri in uri_list])

    def __iter__(self):
        return self.missiles


class ConstLoadPlan(object):
    '''Load plan with constant load'''
    def __init__(self, rps, duration):
        self.rps = rps
        self.duration = duration

    def __iter__(self):
        interval = 1000 / self.rps
        return (i * interval for i in xrange(0, self.rps * self.duration))

    def rps_at(self, t):
        '''Return rps for second t'''
        if t <= self.duration:
            return self.rps
        else:
            return 0

    def duration(self):
        '''Return step duration'''
        self.duration


class AmmoFactoryConfigurator(object):
    def __init__(self, config):
        self.config = config
        self.marker = lambda missile: "None"
        self.filter = lambda missile: True

    def get_load_plan(self):
        return ConstLoadPlan(3, 5)

    def get_missile_generator(self):
        #return SimpleMissileGenerator(HttpAmmo("/", "www.yandex.ru", "GET"))
        return UriStyleMissileGenerator("www.yandex.ru", ["/", "/list", "/all"])

    def get_filter(self):
        return self.filter

    def get_marker(self):
        return self.marker


class AmmoFactory(object):
    '''Link generators, filters and markers together'''
    def __init__(self, config):
        afc = AmmoFactoryConfigurator(config)
        self.load_plan = afc.get_load_plan()
        self.missile_generator = afc.get_missile_generator()
        self.filter = afc.get_filter()
        self.marker = afc.get_marker()

    def __iter__(self):
        return ((timestamp, self.marker(missile), missile.to_s()) for timestamp, missile in zip(self.load_plan, self.missile_generator))

af = AmmoFactory(None)
print(list(af))
