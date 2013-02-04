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
import math
from itertools import cycle, izip, groupby


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


class SimpleMissileGenerator(object):
    '''Generates ammo based on given sample'''
    def __init__(self, missile_sample):
        self.missiles = cycle([(missile_sample.to_s(), None)])

    def __iter__(self):
        return self.missiles


class UriStyleMissileGenerator(object):
    '''Generates GET ammo based on given URI list'''
    def __init__(self, host, uris):
        self.missiles = cycle([(HttpAmmo(uri, host, "GET").to_s(), None) for uri in uris])

    def __iter__(self):
        return self.missiles


class ConstLoadPlan(object):
    '''Load plan with constant load'''
    def __init__(self, rps, duration):
        self.rps = rps
        self.duration = duration

    def __iter__(self):
        interval = 1000000 / self.rps
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

class LineLoadPlan(object):
    '''Load plan with linear load'''
    def __init__(self, minrps, maxrps, duration):
        self.minrps = minrps
        self.maxrps = maxrps
        self.duration = duration

    def __iter__(self):
        k = float(self.maxrps - self.minrps) / self.duration
        b = 1 + 2 * self.minrps / k

        '''
        Solve equation:
        n(t) = k/2 * t^2 + (k/2 + r0) * t
        where r(t) = k(t + 1/2) + r0 -- rps
        r0 is initial rps.
        '''
        def timestamp(n):
            return int((math.sqrt(b * b + 8 * n / k) - b) * 500000) # (sqrt(b^2 + 8 * n / k) - b) / 2 -- time in seconds
        n = 0
        t = timestamp(n)
        while t < self.duration * 1000000:
            yield t
            n += 1
            t = timestamp(n)
        #return (int((math.sqrt(1 + 8 * n / k) - 0.25) * 1000000 / 2) for n in xrange(0, (self.maxrps - self.minrps) * self.duration / 2))

    def rps_at(self, t):
        '''Return rps for second t'''
        if t <= self.duration:
            return self.rps
        else:
            return 0

    def duration(self):
        '''Return step duration'''
        self.duration

class CompositeLoadPlan(object):
    '''Load plan with multiple steps'''
    def __init__(self, steps):
        self.steps = steps

    def __iter__(self):
        base = 0
        for step in self.steps:
            for ts in step:
                yield ts + base
            base += step.duration * 1000000

    def duration(self):
        return sum(step.duration for step in self.steps)


class AmmoFactoryConfigurator(object):
    def __init__(self, config):
        self.config = config

    def get_load_plan(self):
        #return ConstLoadPlan(3, 5)
        #lp = CompositeLoadPlan([ConstLoadPlan(10000, 100), ConstLoadPlan(20000, 200)])
        lp = LineLoadPlan(0, 10, 10)
        return lp

    def get_missile_generator(self):
        #return SimpleMissileGenerator(HttpAmmo("/", "www.yandex.ru", "GET"))
        return UriStyleMissileGenerator("www.yandex.ru", ["/", "/list", "/all"])
        #return AmmoFileReader("/home/direvius/ammo.txt")

    '''Filter. Include missile, if true. Reject on false'''
    def get_filter(self):
        return lambda missile: True

    '''Marker. Mark missile with this tag'''
    def get_marker(self):
        return lambda missile: "None"


class AmmoFactory(object):
    '''Link generators, filters and markers together'''
    def __init__(self, config):
        afc = AmmoFactoryConfigurator(config)
        self.load_plan = afc.get_load_plan()
        self.missile_generator = afc.get_missile_generator()
        self.filter = afc.get_filter()
        self.marker = afc.get_marker()

    def __iter__(self):

# TODO: refactor. We don't know what's inside missile here. Assume it's a string.

        return ((timestamp, marker or self.marker(missile), missile) for timestamp, (missile, marker) in izip(self.load_plan, self.missile_generator))


class StpdWriter(object):
    def __init__(self, config):
        self.af = AmmoFactory(config)

    def generate(self):
        for timestamp, marker, missile in self.af:
            print "%s %s %s\n%s\n" % (timestamp, len(missile), marker, missile)


class AmmoFileReader(object):
    def __init__(self, filename):
        self.ammo_file = open(filename, 'rb')

    def __iter__(self):
        chunk_header = self.ammo_file.readline()
        while chunk_header:
            #chunk_size, marker = chunk_header.split()
            chunk_size = int(chunk_header)

#TODO: return also a marker somehow

            yield (self.ammo_file.read(chunk_size), None)
            chunk_header = self.ammo_file.readline()

            if not chunk_header:
                self.ammo_file.seek(0)
                chunk_header = self.ammo_file.readline()

#lp = CompositeLoadPlan([ConstLoadPlan(3, 3), ConstLoadPlan(2, 2)])
#lp = ConstLoadPlan(3, 5)
#print list(zip(xrange(50), lp))

#af = AmmoFactory(None)
#print(list(af))

#sw = StpdWriter(None)
#sw.generate()

lp = LineLoadPlan(20, 100, 100)
print list((k, len(list(v))) for k, v in groupby(t / 1000000 for t in lp))
