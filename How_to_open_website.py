#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 13:44:50 2020

@author: sudippandey
"""

from selenium import webdriver
chromedriver="/Users/sudippandey/Documents/da_salary_proj/chromedriver"
driver=webdriver.Chrome(chromedriver)
driver.get("http:google.com")