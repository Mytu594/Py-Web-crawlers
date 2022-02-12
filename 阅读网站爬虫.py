# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 15:45:48 2020

@author: Lenovo
"""
import requests

r = requests.get("https://weread.qq.com/web/reader/ce032b305a9bc1ce0b0dd2a")

r.status_code

r.encoding

r.encoding=r.apparent_encoding

r.text
