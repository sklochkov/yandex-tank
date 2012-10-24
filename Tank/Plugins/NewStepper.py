'''
Tools for preparing phantom input data file
'''

from collections import defaultdict
from progressbar import ProgressBar, Percentage, Bar, ETA
import logging
import operator
import os
import re
import tempfile
import tankcore


class HttpAmmo(object):
    def __init__(self, host, method):
        self.method = method
        self.host = host
        self.proto = "HTTP/1.1"
        self.headers = []
        self.body = []


class Generator(object):
    '''The Generator. Gets AmmoFactory and LoadPlan and generates ammo.'''
    def __init__(self, load_plan, ammo_factory):
        self.load_plan = load_plan
        self.ammo_factory = ammo_factory


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

