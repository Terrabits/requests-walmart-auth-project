from pathlib      import Path
from walmart_auth import WalmartSession


# paths
root_path        = Path(__file__).parent.resolve()
private_key_file = root_path / 'secrets' / 'private_key.pem'


# constants
CONSUMER_ID  = '12345678-1234-1234-1234-123456789012'
KEY_VERSION  = '1'
TAXONOMY_URL = 'https://developer.api.walmart.com/api-proxy/service/affil/product/v2/taxonomy'


# read private key
with private_key_file.open('rb') as f:
    private_key = f.read()


# get session
session  = WalmartSession(CONSUMER_ID, private_key, KEY_VERSION)

# get taxonomy
response = session.get(TAXONOMY_URL)
if response.ok:
    print('auth successsful')
else:
    # auth error
    message = response.json()['details']['Description']
    print(f"auth error: '{message}'")
