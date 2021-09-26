import pycurl
import json
import config

from io import BytesIO

client = pycurl.Curl()

client.setopt(client.URL, 'https://svcs.ebay.com/services/search/FindingService/v1')

client.setopt(client.HTTPHEADER, [
    'Accept: application/json',
    'X-EBAY-SOA-OPERATION-NAME: findItemsByKeywords',
    'X-EBAY-SOA-SECURITY-APPNAME: ' + config.appId])

client.setopt(client.POST, 1)
client.setopt(client.POSTFIELDS, json.dumps({
    "findItemsByKeywordsRequest": {
        "xmlns": "http://www.ebay.com/marketplace/search/v1/services",
        "keywords": "vintage shirt"
    }
}))

buffer = BytesIO()
client.setopt(client.WRITEDATA, buffer)
client.perform()

client.close()

body = buffer.getvalue()
print(body.decode('iso-8859-1'))
