import random
import requests


banana = '🍌'
apple = '🍎'
pear = '🍐'

items = [banana, apple, pear]

# Make a random order
order = items[random.randrange(len(items))]


url = "http://127.0.0.1:8000"

response = requests.post(
    url=f'{url}/order',
    params={
        'order': order
    }
)

print(f'Status code: {response.status_code}, order: {order}')
