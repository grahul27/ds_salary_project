# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 19:55:19 2021

@author: gunth
"""

import glassdoor_scraper as gs
import pandas as pd
path="D:/UOA Study & Projects/Data Science Projects/ds_salary_project/chromedriver"

df=gs.get_jobs('data scientist',15,False,path,15)