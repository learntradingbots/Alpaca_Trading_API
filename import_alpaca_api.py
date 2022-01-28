#Import Alpaca Api in Python
import alpaca_trade_api as tradeapi

#Define API connection info from your Alpaca Dashboard
base_url = 'Your API URL'
api_key_id = 'Your API Key'
api_secret_key = 'Your API Secret Key'

#Establish the connection to the Alpaca API
api = tradeapi.REST(
    base_url = base_url,
    key_id = api_key_id,
    secret_key = api_secret
)

#Buy a TSLA Stock
api.submit_order(
    symbol='TSLA',
    qty=1,
    side='buy',
    type='market',
    time_in_force='gtc'
)

#Sell an AAPL Stock
api.submit_order(
    symbol='AAPL',
    qty=1,
    side='sell',
    type='market',
    time_in_force='gtc'
)
