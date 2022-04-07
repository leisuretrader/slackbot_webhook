import ccxt
import time, requests, json

webhook_endpoint = '{your_webhook_endpoint_link}'

# connect to Binance via
exchange = ccxt.binance({
    'apiKey': "",
    'secret': "",
    'enableRateLimit': True,
    'options': {
        'defaultType': 'spot',
    },
})

def current_price(ticker): #BTCUSDT
    fetch_ticker = exchange.fetch_ticker(ticker)
    current_price = fetch_ticker['close']
    return current_price

def send_message(content, webhook): #send message to webhook
    message = {"text": content}
    message_json = json.dumps(message)
    return requests.post(webhook, message_json)

t0 = time.time() + 20  # break the loop after 20 seconds 
while True:
    t1 = time.time()
    t1_format = time.strftime("%H:%M:%S", time.localtime(t1))
    
    if t1 > t0:
        print ('end loop')
        break
    else:
        time.sleep(2)
        text = 'Bitcoin price at {0} is ${1}'.format(t1_format, current_price('BTCUSDT'))
        send_message(text,webhook_endpoint)
