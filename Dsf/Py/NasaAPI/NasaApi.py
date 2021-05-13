import urllib3
from urllib3 import request
import certifi
import pandas as pd
import json

class NasaApi:
    def ShowRequest(self, startDate, endDate, apiKey):
        if endDate != None:
            requestString = "start_date=" + startDate + "&end_date=" + endDate + "&api_key=" + apiKey
        else:
            requestString = "date=" + startDate + "&api_key=" + apiKey
        dataFrame = NasaApi().jsonToDataFrame("https://api.nasa.gov/planetary/apod?" + requestString)

        return dataFrame

    def jsonToDataFrame(self, requestString):
        http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
        r = http.request('GET', requestString)
        data = json.loads(r.data.decode('utf-8'))

        return pd.json_normalize(data)