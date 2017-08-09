# -*- coding: utf-8 -*-

import sys
import yaml

class YamlRead(object):

    def __init__(self):
        f = open('config.yaml')
        content = yaml.load(f)
        self.content = content

    def build(self):
        return self.content
