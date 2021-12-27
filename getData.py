import glassdoor_scraper as gs
import pandas as pd
path="D:/UOA Study & Projects/Data Science Projects/ds_salary_project/chromedriver"

df=gs.get_jobs('data scientist',15,False,path,15)
df.to_csv('glassdoor_jobs.csv',index=False)