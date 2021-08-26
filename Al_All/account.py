import alpaca_trade_api as tradeapi
import tia.dev_auth as authUtil

# authentication and connection details
auth_cred = authUtil.getAlAuth()
api_key = auth_cred['api_key']
api_secret = auth_cred['api_secret']
base_url = auth_cred['base_url']

# instantiate REST API
api = tradeapi.REST(api_key, api_secret, base_url, api_version='v2')

# obtain account information
account = api.get_account()
print(account)
