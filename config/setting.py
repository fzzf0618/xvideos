# -*- coding: utf-8 -*-

import redis
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from util.qiniu_sdk import QiniuSdk
from util.yaml_read import YamlRead

yaml = YamlRead().build()

engine1 = create_engine(yaml['mysql']['url1'])
DBSession = sessionmaker(bind=engine1)

redis = redis.Redis(host=yaml['redis']['host'],port=yaml['redis']['port'],db=0)

qiniu = QiniuSdk()
