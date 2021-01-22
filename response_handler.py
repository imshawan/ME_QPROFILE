# This code was developed to regularly check the responses from user at my site "https://imshawan.netlify.app/"
# Author: Shawan Mandal
# Date: 22-01-2021
#
#


import json
import requests
import pandas as pd


BACKEND_URL = 'MY_BACKEND_URL'

json_response = requests.get(BACKEND_URL).text
json_data = json.loads(json_response)

print("\t\t    Response from visitors \n\n")

df = pd.DataFrame(json_data)  
print(df)

input()