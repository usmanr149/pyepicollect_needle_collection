import pyepicollect as pyep

CLIENT_ID = ***
CLIENT_SECRET = '***'
NAME = 'Needle Colletion'
SLUG = 'needle-collection'

result = pyep.api.search_project(NAME)

token = pyep.auth.request_token(CLIENT_ID, CLIENT_SECRET)

project = pyep.api.get_project(SLUG, token['access_token'])

entries = pyep.api.get_entries(SLUG, token['access_token'], per_page=1000, filter_by='created_at', 
                               filter_from='04/15/2020', filter_to='04/15/2020')
                               
import pandas as pd

df = pd.DataFrame(entries['data']['entries'])

df.sort_values(by=['created_at'], inplace=True)

import pygsheets

gc = pygsheets.authorize('protect/credentials.json')

sh = gc.open_by_key('1J0wALOic45a3wcBUwrbcYDQf4gK5aZWE3FcfVDIMDz4')

wks = sh[0]
# wks.clear(start='A1')

wks.set_dataframe(df=df, start='A1')