import pandas as pd
import numpy as np
import json

from app_store_scraper import AppStore

# add input for which app and id

# compass-real-estate-homes/id692766504
compass = AppStore(country='us', app_name='compass-real-estate-homes', app_id = '692766504')

# amount of reviews we want to save
compass.review(how_many=2000)


compass.reviews

dataFrame = pd.DataFrame(np.array(compass.reviews),columns=['review'])

dataFrameJoined = dataFrame.join(pd.DataFrame(dataFrame.pop('review').tolist()))

dataFrameJoined.head()

dataFrameJoined.to_csv('Compass-app-reviews.csv')
