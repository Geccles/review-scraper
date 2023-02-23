import pandas as pd
import numpy as np
import json
import csv 
from google.oauth2 import service_account
import pygsheets
import os
from dotenv import load_dotenv
load_dotenv()

SHEET_ID = str(os.getenv('SHEET_ID'))

from app_store_scraper import AppStore

# Instead create an array of all and loop over them to grab all reviews
compass = AppStore(country='us', app_name='compass-real-estate-homes', app_id = '692766504')
# amount of reviews we want to save
compass.review(how_many=2000)

compass.reviews

# create dict
dataFrame = pd.DataFrame(np.array(compass.reviews),columns=['review'])
dataFrameJoined = dataFrame.join(pd.DataFrame(dataFrame.pop('review').tolist()))
# Possibly here change to only a certain date range
dataFrameJoined.head()
# Take data and store in csv 
dataFrameJoined.to_csv('Compass-app-reviews.csv')

# BELOW IS ALL GOOGLESHEET LOGIC
with open('service_account.json') as source:
    info = json.load(source)
credentials = service_account.Credentials.from_service_account_info(info)

client = pygsheets.authorize(service_account_file='service_account.json')

sheet = client.open_by_key(SHEET_ID)
wk1 = sheet[0]

wk1.clear()
wk1.set_dataframe(dataFrameJoined, start=(1,1), copy_index=False, copy_head=True, extend=False, fit=False, escape_formulae=False)
