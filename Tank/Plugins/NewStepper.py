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


class HttpAmmo(object):
    def __init__(self, host, method):
        self.method = method
        self.host = host
        self.proto = "HTTP/1.1"
        self.headers = []
        self.body = []


class SimpleAmmoFactory(object):
    '''Generates ammo based on given sample'''
    def __init__(self, ammo_sample):
        self.ammo_sample = ammo_sample

    def get_ammo(self):
        self.ammo_sample


class Generator(object):
    '''
    The Generator. Gets ammo generator and list of timestamps and generates ammo.
    '''
    def __init__(self, timestamps, ammo):
        self.timestamps = timestamps
        self.ammo = ammo


class ConstLoadPlan(object):
    '''Load plan with constant load'''
    def __init__(self, rps, duration):
        self.rps = rps
        self.duration = duration

    def rps(self, t):
        '''Return rps for second t'''
        if t <= self.duration:
            self.rps
        else:
            0

    def duration(self):
        '''Return step duration'''
        self.duration

    def timestamps(self):
        interval = 1000 / self.rps
        (i * interval for i in range(0, self.rps * self.duration))
