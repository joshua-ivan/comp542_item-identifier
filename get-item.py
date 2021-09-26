import pycurl
import config

from io import BytesIO

client = pycurl.Curl()

client.setopt(client.URL, 'https://api.ebay.com/ws/api.dll')

client.setopt(client.HTTPHEADER, [
    'Accept: application/xml',
    'X-EBAY-API-COMPATIBILITY-LEVEL: 1097',
    'X-EBAY-API-DEV-NAME: bar',
    'X-EBAY-API-APP-NAME: ' + config.appId,
    'X-EBAY-API-CERT-NAME: foo',
    'X-EBAY-API-CALL-NAME: GetItem',
    'X-EBAY-API-SITEID: 0'])

itemId = 8675309
client.setopt(client.POST, 1)
client.setopt(client.POSTFIELDS, f'''
<?xml version="1.0" encoding="utf-8"?>
<GetItemRequest xmlns="urn:ebay:apis:eBLBaseComponents">
  <ItemID>{itemId}</ItemID>
</GetItemRequest>
''')

buffer = BytesIO()
client.setopt(client.WRITEDATA, buffer)
client.perform()

client.close()

body = buffer.getvalue()
print(body.decode('iso-8859-1'))
