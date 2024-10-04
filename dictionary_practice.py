s = {
    'name':'GOOG',
    'shares':100,
    'price':490.10
}

print(s)

cost = s['shares']*s['price']
print(cost)


prices = {
 'GOOG' : 490.1,
 'AAPL' : 123.5,
 'IBM' : 91.5,
 'MSFT' : 52.13
 }


if 'IBM' in prices:
    print(prices['IBM'])


print(prices.get('IBM'))

for key in prices.values():
    print(key)


for key in prices:
    print(key)
