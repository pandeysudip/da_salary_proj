#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 00:46:50 2020

@author: sudippandey
"""

import requests
from data_input import data_in
URL = 'http://127.0.0.1:5000/predict'
headers = {"Content-Type": "application/json"}
data ={"input": data_in}

r=requests.get(URL, headers=headers, json=data)

r.json()