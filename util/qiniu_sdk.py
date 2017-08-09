# -*- coding: utf-8 -*-

from util.yaml_read import YamlRead
import urllib
from qiniu import Auth, put_data, etag, urlsafe_base64_encode

## TODO
yaml = YamlRead().build()

class QiniuSdk(object):

    def __init__(self):
        self.access_key = yaml['qiniu']['access_key']
        self.secret_key = yaml['qiniu']['secret_key']
        self.q = Auth(self.access_key, self.secret_key)
        self.bucket_name = yaml['qiniu']['bucket_name']

    def upload(self, url, name):
        token = self.q.upload_token(self.bucket_name, name, 3600)
        url = urllib.urlopen(url)
        ret, info = put_data(token, name, url)
